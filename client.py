import requests 
import streamlit as st

# post request for llama3
def get_llama3_response(url):
    payload = {"url": url}
    response = requests.post(
        "http://localhost:8000/llama3",
        json=payload)
    result = response.json().get('output')
    return result

# post request for gemma2
def get_gemma2_response(url):
    payload = {"url": url}
    response = requests.post(
        "http://localhost:8000/gemma2",
        json=payload)
    result = response.json().get('output')
    return result

st.title('Text Summarizer using Ollama')
url = st.text_input("Enter the URL for summarization:")

# button for llama3
if st.button("Summarize with Llama3"):
    result = get_llama3_response(str(url))
    st.write(result)

# button for gemma2
if st.button("Summarize with Gemma2"):
    result = get_gemma2_response(str(url))
    st.write(result)