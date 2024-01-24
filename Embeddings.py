# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

import openai
import streamlit as st
import pinecone
import time

# Set up a Pinecone instance
pinecone_api_key = st.secrets['pinecone_api_key']
pinecone.init(pinecone_api_key)
# Create an index for storing vectors
# pinecone.create_index(name='fred', dimension=1536)
pinecone_index = pinecone.Index(index_name="fred")
#  dimension=1536, metric="<metric>"

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model).data[0].embedding


with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # st.markdown(message["content"])
        st.markdown(message["content"])
        st.markdown(message["embedding"][:10])

with st.container():
    second_input = st.text_input("Enter additional information here:")

if prompt := st.chat_input("What is up?"):
    embedding = ""
    st.session_state.messages.append({"role": "user", "content": prompt, "embedding": "1"})
    with st.chat_message("user"):
        st.markdown(prompt)
        embedding = get_embedding(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response  + "\n\n" + str(len(embedding)) + str(embedding[:10]))
        timestamp = time.time()

        upsert_response = pinecone_index.upsert(
            vectors=[
                (str(timestamp), embedding, {"prompt":second_input}),
            ]
        )

    st.session_state.messages.append({"role": "assistant", "content": full_response, "embedding": embedding})

