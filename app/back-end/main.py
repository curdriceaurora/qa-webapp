from fastapi import FastAPI,Query
from typing import Annotated
from langchain.document_loaders import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
#os.environ["OPENAI_API_KEY"]
chain = load_qa_chain(llm=OpenAI(), chain_type="map_reduce")

app = FastAPI()

def load_data(dir: str):
    faq = PyPDFLoader(dir)
    return faq.load() 
pdf_path = os.path.join(os.path.dirname(__file__), "example.pdf")
faq = load_data(pdf_path)
@app.get('/faq')
async def show_data():
    return faq[0].page_content

@app.get("/query")
async def qa(q: str):
    return chain.run(input_documents=faq, question=q)
