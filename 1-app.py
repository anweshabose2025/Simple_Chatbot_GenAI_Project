# (D:\Udemy\Complete_DSMLDLNLP_Bootcamp\UPractice1\venv) 
# D:\Udemy\Complete_GenAI_Langchain_Huggingface\UPractice2\Simple_Chatbot>streamlit run 1-app.py

from langchain_groq import ChatGroq 
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

# Groq
import os
from dotenv import load_dotenv 
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")

## streamlit framework
st.set_page_config("🤖 Chatbot")
st.header("👾 Simple Chatbot with GPT-OSS Model")
st.subheader("🖊️ What can I help with?", divider="grey")
input_text=st.chat_input("Ask anything...")

## Ollama Gemma2b model
llm=ChatGroq(model="openai/gpt-oss-120b")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [("system","You are a helpful assistant. Please respond to the question asked"),
     ("user","Question:{context}")])

## Output parser
output_parser=StrOutputParser()

## Chain
chain = prompt | llm | output_parser
#chain = create_stuff_documents_chain(llm=llm,prompt=prompt,output_parser=output_parser)

if input_text:
    response = chain.invoke({"context":input_text})
    st.write(response)
