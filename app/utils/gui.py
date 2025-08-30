import streamlit as st
from app.utils.reader import Reader
from app.config import api 
from asyncio import run
class Gui:
    @staticmethod
    def MainGUI():
        st.set_page_config(page_title="AI Pdf Reader", page_icon="🤖")
        st.header("Text with pdf")
        path = st.file_uploader("Upload your PDF", type=["pdf"])
        if path is not None:
            pdf = Reader(path, api)
            text = run(pdf.extract_text())
            st.divider()
            question = st.text_input("Enter your question here: ")
            if question:
                # retrieve relevant documents from the vector store
                docs = text.similarity_search(question)
                # feed the docs and question to the answer method
                answer = run(pdf.answer(docs, question))
                st.write(answer) 
        else:
            st.info("Please upload a PDF file to proceed.")



