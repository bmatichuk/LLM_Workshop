The purpose of this project is to explore the use of Streamlit in calling Pinecone as method for generating topic vectors from user input. 
This project was set up as part of a workshop originally developed for the Data Management Association (DAMA) of Edmonton and later offered to members of the Data Science Community meetup in Edmonton.
If you are using the project you will note the "secrets" file in the .streamlit folder. 

Here is the format of the directory

<img width="204" alt="image" src="https://github.com/bmatichuk/LLM_Workshop/assets/10739318/a2377c82-7b68-4bf1-981c-9f7e4acf81e1">

The important bit is the secrets file
It should look something like

OPENAI_API_KEY = 'the openai key'
pinecone_api_key = 'the pinecone key'
isaic_key = "the isaic key"

You need to make sure you have those keys. For ISAIC you will need to email them directly to get a key

If you have any questions you can email me at bmatichuk@gmail.com

The Embeddings page purpose is just to show how you can get embeddings from any query to chatgpt and save them in pinecone
Whatever you type in the topic field will be associated with the topic key word meta information associated with that vector in pinecone.
The Topics page just shows you how to get those topic vectors either with or without the topic meta data filter.

