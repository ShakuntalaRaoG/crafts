import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader,TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
import google.generativeai as genai

def get_response_from_AI(prompt):

    GOOGLE_API_KEY = 'AIzaSyA6SJBNzvcZEgtPkV8LlB4YMJCbd3b8Uwg'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response_object = model.generate_content(prompt)
    # added new code from line 14 to 17
    try:
        result = response_object.text
    except Exception as e:
        return response_object
    return result
gunpowder = TextLoader('gunpowder.txt')
TextLoader=('gunpowder.txt')

 
gunpowder.txt = gunpowder.txt.load()
#st.write(data[0].page_content)
gunpowder = gunpowder.txt[0].page_content
response = get_response_from_AI(f""" Trnslate gunpowder into Kannada: {gunpowder}
                     """)

st.write(response)








  

 
