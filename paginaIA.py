import streamlit as st 
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from infomation_b import info


st.title("👁 El super asistente virtual")

if "mesasages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#firt time that the user run the code
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, en que puedo ayudarte?")
    
    st.session_state.messages.append({"role": "assistant", "content": "Hola, en que puedo ayudarte?"})
    st.session_state.first_message = False

if "ollama" not in st.session_state:
    
    template = """

    You are an assistan virtual of the company that I will left you below.
    
    {information_b} is the information of the company.
    You are a virtual assistant of the company {information_b}.

    Answer the question below in spanish

    {context}

    Question: {question}

    Answer:

   """
    model = OllamaLLM(model = "llama3.2")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    context = ""

    

#INPUT

if prompt := st.chat_input("que te puedo ayudar?"):
    
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    resul = chain.invoke({"information_b": info,"context": context, "question": prompt})
        
    with st.chat_message("assistant"):
        st.markdown(resul)
    st.session_state.messages.append({"role": "assistant", "content": prompt})
    context += f"Bot: {resul}\nYou: {prompt}\n"

    
         