import streamlit as mystream
#Installing essential Python libraries who allows you to work with LLMs.

### Storing API keys

#Get Google API key: https://aistudio.google.com (FREE)

import os


os.environ['GOOGLE_API_KEY']  = "DUMMY"

# Using Gemini Models

# Using Google Models (Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# Example of using the Gemini model
# response = gemini_model.invoke("Give me 3 trending AI posts in LinkedIn")

# Display the output
# print(response.content)

# Using Prompt Template

#Prompt templates are pre-designed patterns for creating prompts, with placeholders for specific inputs.


from langchain_core.prompts import PromptTemplate

# Create prompt template for generating tweets

linkedIn_post_template = "Give me {number} posts on {topic} from LinkedIn"

linkedIn_post_prompt = PromptTemplate(template = linkedIn_post_template, input_variables = ['number', 'topic'])

#linkedIn_post_template.format(number =1, topic = "economy")

# Using LLM Chains

#LLM Chains are sequences of prompts and language models combined to perform more complex tasks.

#LLM Chain = Prompt Template | LLM



from langchain_core.prompts import ChatPromptTemplate


# Create LLM chain using the prompt template and model
post_chain = linkedIn_post_prompt | gemini_model

# Example of using the LLM chain
# response = post_chain.invoke({"number" : 2, "topic" : "Generative AI"})

# print(response.content)

# Example of using the LLM chain

# response = post_chain.invoke({"number" : 2, "topic" : "job market in USA"})
# print(response.content)
mystream.header("LinkedIn Post Generator")
mystream.subheader("Find the Trending LinkedIn Post using this App")
topic = mystream.text_input("Topic")
number = mystream.number_input("Provide an input below 10", min_value=1,max_value=10, value=1,step=1)
if mystream.button("Generate Posts"):
  # Example of using the LLM chain
  mypost = post_chain.invoke({"number" : number, "topic" : topic})
  mystream.write(mypost.content)

