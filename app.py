from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemeni pro model and get response
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

def get_gemeni_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.header("খেলা হবে Chatbot")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("লেখো তুমি কি চাও",key="input")
submit = st.button("পাঠাও")

if submit and input:
    response = get_gemeni_response(input)

    ## add user query and response to chat history
    st.session_state['chat_history'].append(("তুমি",input))
    # st.subheader("The response is : ")
    resp = ""
    for chunk in response:
        # st.write(chunk.text)
        # st.session_state['chat_history'].append(("আমি",chunk.text))
        resp += chunk.text
    
    st.session_state['chat_history'].append(("আমি",resp))

st.subheader("The chat history is : ")
for role,text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")