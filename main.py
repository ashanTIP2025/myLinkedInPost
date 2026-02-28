# ============================================================
# LinkedIn Post Generator - Main Application
# A Streamlit app that generates LinkedIn posts using Google's
# Gemini AI model, orchestrated through LangChain.
# ============================================================

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os

# Load the Google API key from Streamlit's secrets manager
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Prompt template
post_template = "Give me {number} LinkedIn posts on {topic}"
post_prompt = PromptTemplate(template=post_template, input_variables=['number', 'topic'])

# Model
gemini_model = ChatGoogleGenerativeAI(model= "gemini-3-flash-preview")

# Chain
post_chain = post_prompt | gemini_model

# UI
st.header("LinkedIn Post Generator")
st.subheader("Generate Trending LinkedIn Posts using Generative AI")

topic = st.text_input("Topic")
number = st.number_input("Number of posts (max 10)", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate Post"):
    linkedInpost = post_chain.invoke({"number": number, "topic": topic})
    content = linkedInpost.content
    if isinstance(content, list):
        text = "".join(block.get("text", "") for block in content if isinstance(block, dict))
    else:
        text = content
    st.write(text)
