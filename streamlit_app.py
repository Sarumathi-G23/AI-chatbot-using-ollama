import streamlit as st
import requests

st.title("")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input box
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post("http://localhost:5000/chat", json={"message": user_input})
        bot_reply = response.json()["response"]
    except Exception as e:
        bot_reply = "⚠️ Error: Unable to connect to chatbot."

    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
