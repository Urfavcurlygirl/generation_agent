import streamlit as st
import youtube_helper as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
        )
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )
        submit_button = st.form_submit_button(label='Submit')

if submit_button and youtube_url and query:
    with st.spinner("Analyzing video..."):
        # 1. Création de la base de données
        db = lch.create_vector_db_from_youtube(youtube_url)

        # 2. Récupération de la réponse
        response, docs = lch.get_response_from_query(db, query)

        st.subheader("Answer:")
        st.write(response)
