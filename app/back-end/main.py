from fastapi import FastAPI, Query, UploadFile, File
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import GooglePalm

import os
import sys  # Import sys for debugging
import google.generativeai as genai

# Use a relative import assuming data_loader.py is in the same directory
from .data_loader import load_data  

import pypdfium2 as pdfium

# Constants
API_KEY_ENV_VAR = 'GEMINI_API_KEY'

# Get the API key from the environment variable
api_key = os.environ.get(API_KEY_ENV_VAR)

# Set your Google Gemini API key
genai.configure(api_key=api_key)

# Assuming GooglePalm class is available in langchain for Gemini
llm = GooglePalm(temperature=0, max_output_tokens=256)
chain = load_qa_chain(llm=llm, chain_type="map_reduce")

app = FastAPI()

# Global variable to store the loaded FAQ data
faq = None

# Debugging: Print the module search path
print(sys.path)

@app.post("/upload")
async def upload_and_process(file: UploadFile = File(...)):
    """Handles file uploads, processes the uploaded PDF, and stores the FAQ data globally."""

    global faq  # Access the global faq variable

    try:
        # Save the uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(file.file.read())

        # Check if the PDF is valid using pypdfium2
        try:
            pdfium.PdfDocument("temp.pdf")
        except pdfium.PdfiumError:
            os.remove("temp.pdf") 
            return {"error": "The uploaded file is not a valid PDF or is corrupted. Please try again with a different file."}

        # Load data from the uploaded file
        faq = load_data("temp.pdf")

        # Clean up the temporary file
        os.remove("temp.pdf")

        return {"message": "File uploaded and processed successfully!"}
    except Exception as e:
        print(f"Error processing uploaded file: {e}")
        return {"error": "An error occurred while processing your file. Please try again or contact support."}

@app.get("/query")
async def qa(q: str) -> dict:
    """Processes a query and returns the answer or an error message."""
    global faq

    if faq is None:
        return {"error": "Please upload a PDF file first."}

    try:
        answer = chain.run(input_documents=faq, question=q)
        if not answer.strip():
            return {"answer": "No relevant information found in the uploaded document. Please try rephrasing your question or uploading a different file."}
        else:
            return {"answer": answer}
    except Exception as e:
        print(f"Error processing query: {e}")
        return {"error": "An error occurred while processing your query. Please try again or contact support."}