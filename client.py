import requests 
import streamlit as st
import time

# post request for llama3
def get_llama3_response(url):
    payload = {"url": url}
    start = time.perf_counter()
    response = requests.post(
        "http://localhost:8000/llama3",
        json=payload)
    result = response.json().get('output')
    elapsed_time = time.perf_counter() - start
    print(f"llama3 inference time: {elapsed_time:.4f} seconds")
    return result

# post request for gemma2
def get_gemma2_response(url):
    payload = {"url": url}
    start = time.perf_counter()
    response = requests.post(
        "http://localhost:8000/gemma2",
        json=payload)
    result = response.json().get('output')
    elapsed_time = time.perf_counter() - start
    print(f"gemma2 inference time: {elapsed_time:.4f} seconds")
    return result

# post request for mistral
def get_mistral_response(url):
    payload = {"url": url}
    start = time.perf_counter()
    response = requests.post(
        "http://localhost:8000/mistral",
        json=payload)
    result = response.json().get('output')
    elapsed_time = time.perf_counter() - start
    print(f"mistral inference time: {elapsed_time:.4f} seconds")
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

# button for mistral
if st.button("Summarize with Mistral"):
    result = get_mistral_response(str(url))
    st.write(result)