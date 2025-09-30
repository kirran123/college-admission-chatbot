import streamlit as st
import openai
import os

openai.api_key = os.getenv("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")

st.set_page_config(page_title="College Admission Chatbot", page_icon="🎓")
st.title("🎓 College Admission Chatbot (GenAI)")

st.markdown("""
Ask me anything about college admissions: eligibility, deadlines, courses, fees, scholarships, and more!
""")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful college admission assistant. Answer questions about college admissions, eligibility, deadlines, courses, fees, and scholarships in a friendly and informative way."}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            max_tokens=512,
            temperature=0.7,
        )
        answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)



