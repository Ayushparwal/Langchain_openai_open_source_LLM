
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import streamlit as st

OPEN_AI_API_KEY="your_api_key"
load_dotenv()

os.environ["OPEN_AI_API_KEY"] = os.getenv("OPEN_AI_API_KEY")
os.environ["langchain_api"] = os.getenv("langchain_api")

# os.environ["LANGCHAIN_TRACING_V2"]=="true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response the the user queries "),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.title("Langchain Demo with OPEN AI")
input_text = st.text_input("Search the topic you want")

#open AI LLM call
llm= ChatOpenAI(model = "gpt-3.5-turbo",api_key=OPEN_AI_API_KEY)
output_parser = StrOutputParser()

#chain making
chain = prompt|llm|output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)