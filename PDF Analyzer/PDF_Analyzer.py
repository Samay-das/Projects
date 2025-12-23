# Importing the require Libraries and the class.
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFLoader
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from pathlib import Path

# Loading the api key from the .env file with the help of load_dotenv() method.
load_dotenv()

# Function to save uploaded file in our working directory.
def save_uploaded_file(uploaded_file, directory="uploaded_files"):
    '''
    Create a uploaded_files directory if not avaiable 
    save the path of the uploaded PDF and try to read
    that PDf from the buffer.
       '''
    if not os.path.exists(directory):
        os.makedirs(directory)
    save_path = Path(directory, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success("PDF file successfully loaded")
    return save_path

# Defining the TextSplitter class so we can split the uploaded document.
class TextSplitter:
    # Intializing the text splitter variable 
    def __init__(self):
        '''
        Intialize the Text Splitter variable with 
        langchain RecursiveCharacterTextSplitter
        method
        '''
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True,
        )
    # Splitting the uploaded document.
    def split(self, docs):
        '''
        Split the document into smaller chunk 
        so can easy for agent to give answer to
        '''
        return self.text_splitter.split_documents(docs)

# Defining the embedding model class for our project.
class Embedding:
    # Intializing the embebbing model.
    def __init__(self):
        '''
        Defining the embedding model (gemini-embedding-001)
        '''
        self.embedded_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

    # Creating the vector store (temperory storage) for our project.
    def create_vector_store(self, pages):
        ''''
        Creating the vector store (temperory storage)
        for our uploaded document.
        '''
        vector_store = InMemoryVectorStore(self.embedded_model)
        vector_store.add_documents(pages)
        return vector_store

#  Loading the pdf with the help of PyPDFLoader.
class PDFLoader:
    def load(self, file_path):
        loader = PyPDFLoader(str(file_path))
        return loader.load()

# Creating an ai agent and also defining the tool for our ai agent.
class Agent:
    # Defining our AI Agent.
    def ai_agent(self, vector_store, query: str):
        # Defining tool for our AI Agent.
        @tool("pdf_search")
        def get_answer(query: str):
            """Retrieve information from the embedded PDF."""
            retrieved_docs = vector_store.similarity_search(query, k=3)
            serialized = "\n\n".join(
                (f"Source: {doc.metadata}\nContent: {doc.page_content}")
                for doc in retrieved_docs
            )
            return serialized

        tools = [get_answer]

        # Giving the system instruction to our AI Agent.
        prompt = "You can use the pdf_search tool to answer user queries from the uploaded PDF."

        # Deining our llm (in our case Google gemini model)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)

        # Binding all together (Tools, LLM, System Instruction)
        agent = create_agent(tools=tools, model=llm, system_prompt=prompt)

        # Storing our agent output in the variable.
        output = None
        for event in agent.stream(
            {"messages": [{"role": "user", "content": query}]},
            stream_mode="values",
        ):
            output = event["messages"][-1].content

        return output


# Creating a Front-end with th3e help of streamlit framework.
st.title("PDF Analyzer")

# Taking the pdf from the end user.
with st.form(key="pdf_upload_section"):
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        uploaded_file_path = save_uploaded_file(uploaded_file)
    st.form_submit_button(label="Submit")

# After Pdf loaded by the end user.
if uploaded_file is not None:

    # Creating a object for our above defined classes. 
    pdf_loader = PDFLoader()
    emb_model = Embedding()
    txt_splitter = TextSplitter()

    # Calling the method from the appropriate object.
    pdf_docs = pdf_loader.load(uploaded_file_path)
    pdf_pages = txt_splitter.split(pdf_docs)
    vector_store = emb_model.create_vector_store(pdf_pages)

    # Calling our AI Agent.
    agent = Agent()

    # Taking the query from the end user.
    user_query = st.chat_input("Ask your query here!!")
    if user_query:
        agent_output = agent.ai_agent(vector_store, user_query)
        with st.chat_message("ai"):
            st.write(agent_output)

    # Giving the option to delete the previous loaded pdf.
    with st.sidebar:
        if st.button("Clear Memory"):
            file_path = str(uploaded_file_path)
            if os.path.exists(file_path):
                os.remove(file_path)
                st.success("PDF successfully removed")