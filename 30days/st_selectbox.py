import streamlit as st

st.header('Learn st.selectbox')

option = st.selectbox(
    "What's your favorite color?",
    ('Blue', 'Teal', 'Lavender')
)

st.write('My favorite color is: ', option)
