import requests 
import streamlit as st

def get_ollama_response(url):
    payload = {"url": url}
    response = requests.post(
        "http://localhost:8000/ollama",
        json=payload)
    result = response.json().get('output')
    return result

st.title('Text Summarizer with LLAMA3 using Ollama')
url = st.text_input("Enter the URL for summarization:")

if st.button("summarize"):
    result = get_ollama_response(str(url))
    st.write(result)