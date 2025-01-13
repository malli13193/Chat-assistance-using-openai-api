



import streamlit as st
import openai
import PyPDF2
import tiktoken

# Initialize OpenAI API key
# openai.api_key = "your_openai_api_key"
openai.api_key = "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"


def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def chunk_text(text, max_tokens=1000):
    """Chunk text into manageable pieces based on token limits."""
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = tokenizer.decode(tokens[i:i + max_tokens])
        chunks.append(chunk)
    return chunks

def get_relevant_chunk(query, chunks):
    """Find the most relevant chunk of text for a query."""
    relevance_scores = []
    for chunk in chunks:
        prompt = f"Rate the relevance of the following text for answering the query:\n\nQuery: {query}\nText: {chunk}\n\nRespond with a score from 0 to 1, where 1 is highly relevant."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for evaluating relevance."},
                {"role": "user", "content": prompt}
            ]
        )
        score = float(response.choices[0].message["content"].strip())
        relevance_scores.append(score)
    best_chunk = chunks[relevance_scores.index(max(relevance_scores))]
    return best_chunk

def generate_response(query, chunk):
    """Generate a response using OpenAI API."""
    prompt = f"Based on the provided text, answer the following question:\n\nText: {chunk}\n\nQuestion: {query}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful support agent for CDP."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

# Streamlit UI
st.title("CDP Support Agent Chatbot")
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Upload your CDP documentation (PDF)", type="pdf")

if uploaded_file:
    # Extract and chunk PDF content
    st.sidebar.success("PDF uploaded successfully!")
    with st.spinner("Processing the PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(pdf_text)
    
    st.success("PDF processed successfully!")

    # Input for user query
    query = st.text_input("Ask a 'how-to' question about CDP:")
    if query:
        with st.spinner("Finding the best answer..."):
            relevant_chunk = get_relevant_chunk(query, chunks)
            answer = generate_response(query, relevant_chunk)
        
        st.subheader("Answer:")
        st.write(answer)
