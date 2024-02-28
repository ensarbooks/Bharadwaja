import os
import streamlit as st
from langchain_openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()
 
# Function to return the response
def load_answer(question):
    api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(api_key=api_key, temperature=0.7)
    answer = llm(question)
    return answer
 
# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")
 
# Function to get user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text
user_input = get_text()
 
# If generate button is clicked
if st.button('Generate'):
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)