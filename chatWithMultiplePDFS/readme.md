Chat with PDF using Gemini
A Streamlit-based application that allows users to interactively ask questions about the content of PDF files. 
Leveraging Google's Gemini Pro  model and LangChain, this app processes PDF files, creates vector embeddings, and provides detailed answers to user queries based on the document content.

Features
PDF Text Extraction: Upload multiple PDF files and extract their text content.
Text Chunking: Split extracted text into manageable chunks for efficient processing.
Vector Store Creation: Create and store vector embeddings of the text chunks using FAISS.
Interactive Q&A: Ask questions based on the PDF content and receive detailed responses.
Streamlit Interface: User-friendly interface for easy interaction.

How It Works
Upload Your PDF Files: Use the sidebar to upload one or multiple PDF files.
Process PDF Files: Click the "Submit & Process" button to extract text and create vector embeddings.
Ask Questions: Enter your question in the input field and get detailed answers based on the PDF content.
