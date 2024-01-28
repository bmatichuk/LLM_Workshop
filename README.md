The purpose of this project is to explore the use of Streamlit in calling Pinecone as method for generating topic vectors from user input. 
This project was set up as part of a workshop originally developed for the Data Management Association (DAMA) of Edmonton and later offered to members of the Data Science Community meetup in Edmonton.
If you are using the project you will note the "secrets" file in the .streamlit folder. 

Here is the format of the directory

<img width="217" alt="image" src="https://github.com/bmatichuk/LLM_Workshop/assets/10739318/3aa4cced-ff6e-4e13-8749-ac68dcb21b8f">


The important bit is the secrets file
Note I am not giving you my keys - you have to go get those yourself.

It should look something like

OPENAI_API_KEY = 'the openai key' <p>
pinecone_api_key = 'the pinecone key' <p>
isaic_key = "the isaic key"

You need to make sure you have those keys. For ISAIC you will need to email them directly to get a key

use https://openai.com to get an api key for openai <p>
use https://pinecone.io to get an api key for pinecone <p>
use https://isaic.ca to get the api for isaic

If you have any questions you can email me at bmatichuk@gmail.com

The Embeddings page purpose is just to show how you can get embeddings from any query to chatgpt and save them in pinecone
Whatever you type in the topic field will be associated with the topic key word meta information associated with that vector in pinecone.
The Topics page just shows you how to get those topic vectors either with or without the topic meta data filter.

