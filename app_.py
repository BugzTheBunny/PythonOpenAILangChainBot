from langchain_openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

st.set_page_config(page_title="QA Bot")
MODEL = "gpt-3.5-turbo-instruct"
load_dotenv()


def get_model(model_name: str) -> OpenAI:
    return OpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model=model_name,
        temperature=1
    )


def get_openai_response(open_ai_llm: OpenAI, question: str):
    if question:
        return open_ai_llm.invoke(question)


openai_llm = get_model(MODEL)

with st.form("bot_form"):
    user_input = st.text_input(label="I Wanna ask...")
    ask = st.form_submit_button("Ask!")

    if ask:
        response = get_openai_response(openai_llm, user_input)
        st.write(response)
