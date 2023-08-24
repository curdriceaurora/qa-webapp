import streamlit as st
import requests

api_url = 'http://127.0.0.1:8000/faq'
st.title('Enter a question')

user_input = st.text_input("Enter some input:",placeholder = 'question')
if user_input:

    api_url = 'http://127.0.0.1:8000/query'

    params = {"q": user_input}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        api_data = response.json()
        st.write(api_data)
    else:
        st.write(response.status_code)
