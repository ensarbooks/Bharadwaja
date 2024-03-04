import os
from langchain_openai import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
 
load_dotenv()
 
# UI
st.title("Translator")
language_type = st.sidebar.selectbox("What is your language?", ("Telugu", "Tamil", "Hindi","English"))
input_text = st.text_input("Enter the text")
button = st.button("Generate Response")
 
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API Key is missing. Please set it in the environment variables.")
 
# llms
llm = OpenAI(api_key=openai_api_key, temperature=0.7)
 
prompt_template = PromptTemplate(
    input_variables=['sentence'],
    template="In an easy way translate the following sentence {sentence} into " + language_type
)
 
chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)
 
if input_text:
    st.write(chain.run(input_text))