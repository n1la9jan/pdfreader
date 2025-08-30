from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import GoogleGenerativeAI as Gemini
class Reader:
    def __init__(self, path, api):
        self.path = path
        self.api = api

    async def extract_text(self) -> str:
        reader = PdfReader(self.path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
        chunks = text_splitter.split_text(text)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=self.api)
        document = FAISS.from_texts(chunks, embeddings)
        return document 
    
    async def answer(self, docs, query) -> str:

        llm = Gemini(model="models/gemini-2.5-flash", google_api_key=self.api)
        chain = load_qa_chain(llm, chain_type="stuff")
        result = chain.run(input_documents=docs, question=query)
        return result