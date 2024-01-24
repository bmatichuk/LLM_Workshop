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

anytopic = False
if st.checkbox('Any Topic'):
    anytopic = True

with st.container():
    second_input = st.text_input("Enter topic string here:")

query_response = ""
combo = ""

if prompt := st.chat_input("What is up?"):
    embedding = ""
    st.session_state.messages.append({"role": "user", "content": prompt, "embedding": "1"})
    with st.chat_message("user"):
        st.markdown(prompt)
        embedding = get_embedding(prompt)      
        if anytopic == True:
            query_response = pinecone_index.query(
                vector=embedding,
                top_k=5,
                include_values=False,
                include_metadata=True,
            )
        else:
            query_response = pinecone_index.query(
                vector=embedding,
                top_k=5,
                include_values=False,
                include_metadata=True,
                filter={"prompt": {"$eq": second_input}}
            )         
        st.markdown(str(query_response))
