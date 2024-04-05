
import streamlit as st
from openai_utils.openai_models_selection import model_selection
from openai_utils.openai_chat_interface import chat_interface
from openai_utils.openai_api_utils import openai_setup
from config import config
from intro import intro

st.sidebar.title("Settings :gear:")


side_bar_dynamic = {
    "Introduction":intro,
    "Model Selection":model_selection
}


if "openai_model" not in st.session_state:
    # Get the first key in the outer dictionary
    default_model = next(iter(config['openai_chat_model']))
    st.session_state["openai_model"] = default_model

if "messages" not in st.session_state:
    st.session_state.messages = []

OPENAI_API_KEY = st.sidebar.text_input("Enter OPENAI API KEY", type="password")
if OPENAI_API_KEY:
    
    st.sidebar.write("Woah! Let's get chatting! 🎉")
    using_openai_model = st.session_state["openai_model"]
    st.sidebar.subheader("Assistant Version:")
    st.sidebar.write(f":green[{using_openai_model}]")

else:
    st.sidebar.write("Hey there! Provide me with your API key to unlock our chat adventure! 🔐")

setting_mode = st.sidebar.selectbox("Choose Setting",side_bar_dynamic.keys())

side_bar_dynamic[setting_mode]()

if setting_mode !="Introduction":
    intro()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if OPENAI_API_KEY:
    
    api_key=OPENAI_API_KEY
    client = openai_setup(api_key=api_key)
    
    chat_interface(client=client, model=using_openai_model)

else:
    st.session_state.messages = []