# Text Summarizer Webapp

## Introduction

This is a simple webapp for text summarization, where the user can input the url for an article,
and the article will be summarised into concise bullet points.

It currently can be done with the Llama3 and Gemma2 models from [Ollama](https://github.com/ollama/ollama/)
that are optimized to be run locally on your own device.

The `serve.py` contains the server-side code that uses [FastAPI](https://github.com/tiangolo/fastapi), a web framework for quickly building APIs with Python.\
The `client.py` contains the client-side code that uses [Streamlit](https://github.com/streamlit/streamlit), to quickly transform Python scripts into interactive web apps.\
The `text-summarizer.ipynb` jupyter notebook file in the `tests` folder can be used for testing purposes.

## Steps to run the Webapp

1. install ollama from [ollama-python](https://github.com/ollama/ollama-python)
2. run `ollama pull gemma2` to download the model locally
3. run `ollama pull llama3` to download the model locally
4. run `ollama serve` to start the server on a terminal
5. run `pip install -r requirements.txt` to install required libraries for the project
6. run `streamlit run backend/serve.py` for backend server on a second terminal
7. run `streamlit run client.py` for frontend client on a third terminal
