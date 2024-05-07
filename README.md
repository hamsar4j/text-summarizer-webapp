# text-summarizer-webapp

**Introduction**
This is a simple webApp for text summarization where user can input a url for an article,
and the summary will be returned to the user as the output.

Currently, it uses the LLama3 LLM model from Ollama that is optimized to be run locally on
your own device.

The text-summarizer.ipynb jupyter notebook file can be used for testing purposes.

**Steps to run webApp**

1. install ollama from https://github.com/ollama/ollama-python
2. run "ollama serve" to start the server
3. run "ollama pull llama2" to download the model locally
4. run "pip install -r requirements.txt" to install required libraries for the project
5. run "streamlit run serve.py" for backend server
6. run "streamlit run client.py" for frontend
