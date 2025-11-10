# (D:\Udemy\Complete_DSMLDLNLP_Bootcamp\UPractice1\venv) 
# D:\Udemy\Complete_GenAI_Langchain_Huggingface\UPractice2\Simple_Chatbot>streamlit run 1-app.py
# python = 3.13

from langchain_groq import ChatGroq 
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

## streamlit framework
st.set_page_config("🤖 Chatbot")
st.sidebar.title("Settings")
st.header("🌐 Simple Q&A Chatbot With Groq")
st.subheader("🖊️ What can I help with?", divider="grey")
input_text=st.chat_input("Ask anything...")

groq_api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")
engine=st.sidebar.selectbox("Select Open Source model",["openai/gpt-oss-120b","openai/gpt-oss-20b"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7) # value=0.7: default temperature
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150) # value=150: default max_tokens

if not groq_api_key:
    st.warning("Please enter the api key")

if not input_text:
    st.warning("Please enter the text")

if input_text and groq_api_key:
    ## Ollama Gemma2b model
    llm=ChatGroq(model=engine,api_key=groq_api_key) #,temperature=temperature,max_tokens=max_tokens)

    ## Prompt Template
    prompt=ChatPromptTemplate.from_messages(
        [("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{context}")])

    ## Output parser
    output_parser=StrOutputParser()

    ## Chain
    chain = prompt | llm | output_parser

    response = chain.invoke({"context":input_text})
    st.write(response)
