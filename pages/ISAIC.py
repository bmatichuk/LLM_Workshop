import streamlit as st
import os

import requests
import json

# URL from the curl command
url = "https://api-llama.isaic.ai/api/generate"

# Headers from the curl command
headers = {
    "Authorization": "Basic QlJVQ0U6TEJWUHlNeW52YXdlUzNZWllwOHVBTHRPbDdNVWF2em03SnVDMk5mZkJmZEV2dFFiRjdfOV9DeVM2YW9jNmxNcmRzcFZyM0taVEhTcjhoU0N0VVlYU1hxS0ktc0xRWUl0M1gtX2tTQXUwMUFldTNRVGZvM01xS0ZKVmd4R1c4WEdZWnRQR2hPS0k5aU9wRXY0TmNDUWxmRzVQdlBIaHVhWVdwcFR1ZmlPVmVF"
}



# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    # Make the POST request and get the response

    data = {
        "model": "llama2",
        "stream": False,
        "prompt": f"{string_dialogue} {prompt_input} Assistant: "
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response = response.json()
    return response



if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    embedding = ""
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    message_placeholder = st.empty()
    full_response = ""
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            # response=json.dumps(response)
            placeholder = st.empty()
            item_response = ""
            #for item in response:
            #    item_response += item
            # for item in item_response:
            item_response += response.get("response", "")
    full_response = {"role": "assistant", "content": item_response}
    message_placeholder.markdown(item_response)

    st.session_state.messages.append({"role": "assistant", "content": item_response})

