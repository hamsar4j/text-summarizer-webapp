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
llm = Ollama(model="llama3")

# convert chat message to string
output_parser = StrOutputParser()

# combine into LLM chain
chain = prompt | llm | output_parser

# function to get text from webpage
def get_docs(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs

class Url(BaseModel):
    url: str

# function to summarise text
@app.post("/ollama")
async def summarize_text(url: Url):
    text = str(url.url)
    input_text = get_docs(text)
    result = chain.invoke({'input': input_text})
    return {'output': result}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)