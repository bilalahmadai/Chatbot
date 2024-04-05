import streamlit as st
from config import config
def model_selection():
    
    
    with st.sidebar:
        
        avaiable_openai_model = []

        for openai_model in config['openai_chat_model']:
            avaiable_openai_model.append(openai_model)

        openai_chat_model = st.selectbox("Select Model",avaiable_openai_model)
        with st.expander("See Model Details"):
            if openai_chat_model:
                description =  config['openai_chat_model'][openai_chat_model]['DESCRIPTION']
                st.markdown(":green[DESCRIPTION]")
                st.markdown(description)

                context_window =  config['openai_chat_model'][openai_chat_model]['CONTEXT WINDOW']
                st.markdown(":green[CONTEXT WINDOW]")
                st.markdown(context_window)

                training_data =  config['openai_chat_model'][openai_chat_model]['TRAINING DATA']
                st.markdown(":green[TRAINING DATA]")
                st.markdown(training_data)
    
    
    st.session_state["openai_model"] = openai_chat_model
