from langchain.document_loaders import PyPDFLoader
import os

def load_data(file_path):
    """
    Loads data from a PDF file using PyPDFLoader.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        list: A list of Document objects representing the loaded data.
    """

    loader = PyPDFLoader(file_path)
    return loader.load()

# You can add additional data loading or preprocessing logic here if needed.