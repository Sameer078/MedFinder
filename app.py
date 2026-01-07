import streamlit as st
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS


from dotenv import load_dotenv
load_dotenv() 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

# --- Use ChromaDB ---

# def create_vector_db():
#     loader = CSVLoader(file_path='drugs_side_effects_drugs_com.csv', encoding="utf-8", csv_args={'delimiter': ','})
#     data = loader.load()
#     Chroma.from_documents(data, embeddings,persist_directory="./chroma_db")

# def get_conversational_chain():
#     prompt_template = """
#     Answer the question from the provided context, make sure to provide all correct details, if the answer is not in
#     provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
#     Context:\n {context}?\n 
#     Question: \n{question}\n
#     Answer:
#     """
#     vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
#     retriever = vectordb.as_retriever(score_threshold=0.7)
#     model = ChatGoogleGenerativeAI(model="gemini-pro",
#                              temperature=0.3)

#     prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
#     chain=RetrievalQA.from_chain_type(llm=model,
#                                         chain_type="stuff",
#                                         retriever=retriever,
#                                         input_key="query",
#                                         return_source_documents=True,
#                                         chain_type_kwargs={"prompt": prompt})
#     return chain

# st.set_page_config(page_title='Drug Chatbot',page_icon='<>',layout='centered')
# st.header('Drug Chatbot')
# inputtext =st.text_input('How do i help you?')
# submit=st.button('Submit')

# if submit:
#     chain=get_conversational_chain()
#     response=chain(inputtext)
#     st.header("Answer")
#     st.write(response["result"])



# --- Use FAISS ---

# def get_vector_store():
#     loader = CSVLoader(file_path='drugs_side_effects_drugs_com.csv', encoding="utf-8", csv_args={'delimiter': ','})
#     data = loader.load()
#     vector_store = FAISS.from_documents(data, embedding=embeddings)
#     vector_store.save_local("faiss_index")

# def get_qa_chain():
#     vectordb = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
#     retriever = vectordb.as_retriever(score_threshold=0.7)

#     prompt_template = """Given the following context and a question, generate an answer based on this context only.
#     In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
#     If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

#     CONTEXT: {context}

#     QUESTION: {question}"""

#     PROMPT = PromptTemplate(
#         template=prompt_template, input_variables=["context", "question"]
#     )
#     model = ChatGoogleGenerativeAI(model="gemini-pro",
#                              temperature=0.3)
#     chain = RetrievalQA.from_chain_type(llm=model,
#                                         chain_type="stuff",
#                                         retriever=retriever,
#                                         input_key="query",
#                                         return_source_documents=True,
#                                         chain_type_kwargs={"prompt": PROMPT})
#     return chain

# st.set_page_config(page_title='Drug Chatbot',page_icon='<>',layout='centered')
# st.header('Drug Chatbot')
# inputtext =st.text_input('How do i help you?')
# submit=st.button('Submit')

#for making vector store -->
# if submit:
#     create_vector_db()

# for making faiss vector store -->
# if submit:
#     get_vector_store()

#for faiss Q&A
# if submit:
#     chain=get_qa_chain()
#     response=chain(inputtext)
#     st.header("Answer")
#     st.write(response["result"])
