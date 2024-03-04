import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
 
load_dotenv()
 
#UI
st.title("Celebrity Search Results")
input_text = st.text_input("Search the celebrity You want!!!")
button = st.button("Generate Response")
 
#prompt template
first_prompt = PromptTemplate(
    input_variables=['name'],
    template= "Tell me about {name}"
)
 
#llms
llm = OpenAI(temperature=0.8)
 
chain = LLMChain(llm=llm, prompt=first_prompt, verbose=True, output_key="person")
 
second_prompt = PromptTemplate(
    input_variables=['person'],
    template= "when was the {person} born"
)
 
chain2 = LLMChain(llm=llm,prompt=second_prompt, verbose=True, output_key="dob")
 
third_prompt = PromptTemplate(
    input_variables=['dob'],
    template= "mention 5 major events happened on {dob} in the world"
)
 
chain3 = LLMChain(llm=llm, prompt=third_prompt, verbose=True, output_key="description")
 
 
parent_chain = SequentialChain(
    chains=[chain,chain2,chain3], input_variables=['name'], output_variables=['person','dob','description'],verbose=True
)
 
if input_text:
    st.write(parent_chain({'name':input_text}))
 