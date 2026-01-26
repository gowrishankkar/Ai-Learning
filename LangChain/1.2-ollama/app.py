import os
from dotenv import load_dotenv
import requests

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# LangSmith tracking is optional, so guard missing values.
def configure_langsmith():
    langsmith_key=os.getenv("LANGCHAIN_API_KEY")
    if langsmith_key:
        os.environ["LANGCHAIN_API_KEY"]=langsmith_key
        os.environ["LANGCHAIN_TRACING_V2"]="true"
        project=os.getenv("LANGCHAIN_PROJECT")
        if project:
            os.environ["LANGCHAIN_PROJECT"]=project


def resolve_llm(model_name="gemma3:270m"):
    try:
        response=requests.get("http://127.0.0.1:11434/api/tags",timeout=3)
        response.raise_for_status()
        return Ollama(model=model_name)
    except Exception:
        st.error("Ollama is unavailable. Start it with 'ollama serve' or update the model settings.")
        return None


configure_langsmith()

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm=resolve_llm()
output_parser=StrOutputParser()

chain=None
if llm:
    chain=prompt|llm|output_parser

if input_text and chain:
    st.write(chain.invoke({"question":input_text}))

if input_text and not chain:
    st.stop()


