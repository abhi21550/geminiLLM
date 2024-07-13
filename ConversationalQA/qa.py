from dotenv import load_dotenv
import streamlit as st

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-pro")

chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input= st.text_input("Input:",key="input")
submit=st.button("ASK")

if submit and input:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("YOU",input))
    st.subheader("RESPONSE")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("CHAT HISTORY")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")



