from openai import OpenAI
import streamlit as st

def openai_setup(api_key):
    client = OpenAI(api_key=api_key)
    return client




def openai_chat_completion_st_stream(client,model):
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        return stream
    except Exception as e:
        st.error(f"OpenAI API error: {e}")
        return None
