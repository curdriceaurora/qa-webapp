import streamlit as st
import requests

# Constants
API_URL = 'http://127.0.0.1:8000/query'
UPLOAD_API_URL = 'http://127.0.0.1:8000/upload'

# Function to fetch data from the backend
def fetch_answer(query: str) -> str | None:
    """Fetches the answer to a query from the backend API.

    Args:
        query (str): The user's question.

    Returns:
        str | None: The answer to the question, or None if there was an error.
    """

    params = {"q": query}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            st.error(data['error'])
            return None
        else:
            return data['answer']
    else:
        st.error("Oops! Something went wrong. Please try again later.")
        return None

# Streamlit app
st.title('🦜 Ask Questions About Our Product 🦜')
st.write("""
Welcome! I'm here to answer your questions about our product. 
Feel free to ask anything related to features, pricing, or how to get started. 
I'll do my best to provide you with accurate and helpful information.

**Example Questions:**

* What are the key features of your product?
* How much does your product cost?
* Is there a free trial available?
""")

# Input validation
user_input = st.text_input("Your Question:", placeholder="Type your question here...")
if not user_input:
    st.warning("Please enter a question.")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

# Use session state to store responses
if 'responses' not in st.session_state:
    st.session_state.responses = {}

if st.button('Get Answer') and user_input:
    if uploaded_file is not None:
        # Send the uploaded file to the backend
        files = {'file': uploaded_file}
        response = requests.post(UPLOAD_API_URL, files=files)

        if response.status_code == 200:
            data = response.json()
            if 'error' in data:
                st.error(data['error'])
                st.warning("Please choose a different PDF file.")
            else:
                # Process the response from the backend 
                answer = fetch_answer(user_input) 
                if answer:
                    st.markdown(f"**Answer:** {answer}")
                else:
                    st.error("😔 Sorry, I couldn't find an answer to your question in the uploaded document. Please try rephrasing it or uploading a different file.")
        else:
            st.error("Error uploading file. Please try again.")
    else:
        st.warning("Please upload a PDF file first.")