from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from fastapi import FastAPI
from langserve import add_routes
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title = 'LangChain Server',
    version = '1.0',
    description = "A simple API server using LangChain's Runnable interfaces"
)

# prompt templates convert raw user input to better input for the LLM
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class text summariser who will provide concise summaries in bullet points."),
    ("user", "{input}")
])

# choose llm
llama3 = Ollama(model="llama3:8b-instruct-q4_0")
gemma2 = Ollama(model="gemma2:9b-instruct-q4_0")
mistral = Ollama(model="mistral:instruct")

# convert chat message to string
output_parser = StrOutputParser()

# combine into LLM chain
llama3_chain = prompt | llama3 | output_parser
gemma2_chain = prompt | gemma2 | output_parser
mistral_chain = prompt | gemma2 | output_parser

# function to get text from webpage
def get_docs(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs

class Url(BaseModel):
    url: str

# function to summarise text
@app.post("/llama3")
async def summarize_text_llama3(url: Url):
    text = str(url.url)
    input_text = get_docs(text)
    result = llama3_chain.invoke({'input': input_text})
    return {'output': result}

@app.post("/gemma2")
async def summarize_text_gemma2(url: Url):
    text = str(url.url)
    input_text = get_docs(text)
    result = gemma2_chain.invoke({'input': input_text})
    return {'output': result}

@app.post("/mistral")
async def summarize_text_mistral(url: Url):
    text = str(url.url)
    input_text = get_docs(text)
    result = mistral_chain.invoke({'input': input_text})
    return {'output': result}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)