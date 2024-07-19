# Text Summarizer Webapp

## Introduction

This is a simple webapp for text summarization, where the user can input the url for an article,
and the article will be summarised into concise bullet points.

I was experimenting with the time taken for inference by each of the models to summarise an article from a webpage
to quantitatively analyze their efficiency on my local 16gb ram macbook air.

It was done with the llama3:8b-instruct-q4_0, gemma2:9b-instruct-q4_0 & mistral:instruct_q4 models from [Ollama](https://github.com/ollama/ollama/) that are optimized to be run locally on your own device.

The `serve.py` contains the server-side code that uses [FastAPI](https://github.com/tiangolo/fastapi), a web framework for quickly building APIs with Python.\
The `client.py` contains the client-side code that uses [Streamlit](https://github.com/streamlit/streamlit), to quickly transform Python scripts into interactive web apps.\

## Steps to run the Webapp

1. install ollama from [ollama-python](https://github.com/ollama/ollama-python)
2. run `ollama pull gemma2:9b-instruct-q4_0` to download the model locally
3. run `ollama pull llama3:8b-instruct-q4_0` to download the model locally
4. run `ollama pull mistral:instruct` to download the model locally
5. run `ollama serve` to start the server on a terminal
6. run `pip install -r requirements.txt` to install required libraries for the project
7. run `streamlit run backend/serve.py` for backend server on a second terminal
8. run `streamlit run client.py` for frontend client on a third terminal
