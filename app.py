import streamlit as st
from rag_pipeline import get_response

st.title("EcoTrack AI – Waste Segregation Assistant")

user_query = st.text_input("Ask how to dispose any waste:")

if user_query:
    response = get_response(user_query)
    st.write("### AI Recommendation:")
    st.write(response)
