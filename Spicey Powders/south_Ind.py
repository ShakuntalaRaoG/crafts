

import streamlit as st
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

text = """Chatnipudi ingredients:-

* chanadal  1 cup,
* Udad dal 3/4 cup,
* Tuvar dal 1/2 cup,
* Dry mirchi 20-25(according to your taste),
* Dry copra  grated 1/2 cup,to fry in low flame for 2 minutes.
* Tamarind- approximately one lemon size,
* Jagary (gud) one tea spoon,
* Hing 1/2 tea spoon,
* Haldi 1 spoon.

* To dry roast 1,2,3,4 separately until golden brown.
* To add the other ingredients. 
* After they come to room temperature, to put in a mixer and powder coarsely.  
* Lastly heat one table spoon of oil and put mustard s.)"""

response = get_response_from_AI(f"""Translate this text in English. Text : {text}
                     """)

st.write(response)








  

 
