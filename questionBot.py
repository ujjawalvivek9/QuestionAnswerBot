import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(user_input):
    if user_input.strip() != "":
        response = chat.send_message(user_input)
        return response.text
    else:
        return "Please enter a question."

st.set_page_config(page_title="Q&A", page_icon="🤖")
st.header("Gemini LLM Application for Q&A")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)

    st.session_state["chat_history"].append(("you", user_input))
    st.session_state["chat_history"].append(("bot", response))

    st.subheader("Response:")
    st.write(response)

st.subheader("Chat History:")
for role, text in st.session_state["chat_history"]:
    if role == "you":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")