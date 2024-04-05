import streamlit as st
from .openai_api_utils import openai_setup, openai_chat_completion_st_stream



def chat_interface(client, model):
    
    if prompt := st.chat_input("Let's chat!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                stream = openai_chat_completion_st_stream(client=client, model=model)
                if stream is not None:
                    response = st.write_stream(stream)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                else:
                    st.error("Oops! 😅 I couldn't summon my assistant. Check your API key and let's try again! 🔑")
            except Exception as e:
                st.error(f"OpenAI API error: {e}")
