# **CDP Support Agent Chatbot**

A chatbot designed to assist users with "how-to" questions about CDP (Customer Data Platforms) by analyzing uploaded PDF documents. It uses the OpenAI API (`gpt-3.5-turbo`) to process and respond to queries intelligently.

---

## **Features**
- Upload a PDF document containing CDP documentation.
- Automatically process and chunk the PDF text for efficient querying.
- Ask "how-to" questions and get accurate responses based on the document content.
- User-friendly interface built with Streamlit.

---

## **System Requirements**
- Python 3.7 or later.
- A valid OpenAI API key.

---

## **Accuracy**
The chatbot utilizes OpenAI's `gpt-3.5-turbo` model, which is highly accurate for natural language understanding and text generation tasks. 

![image](https://github.com/user-attachments/assets/32868d90-a7ee-4605-8ce2-0fd167f63279)


### **Performance Insights**
- **Contextual Relevance**: The bot selects the most relevant sections from the PDF to answer user queries.
- **Response Precision**: Achieves a high level of precision, especially when provided with well-structured documentation.

> **Note**: The accuracy depends on the quality and relevance of the uploaded PDF document. Complex queries outside the scope of the document may result in less accurate answers.

---

## **Setup Instructions**
Follow these steps to clone and run the project locally.

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/cdp-support-agent-chatbot.git
cd cdp-support-agent-chatbot
