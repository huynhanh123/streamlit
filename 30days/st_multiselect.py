import streamlit as st

st.header ('Learn st.multiselect')

options = st.multiselect (
    'What are food do you want to eat?',
    ['Bun rieu', 'Bun bo', 'Banh uot', 'Com tam', 'Pizza'] ,
    ['Bun rieu', 'Bun bo', 'Banh uot']
)
st.write('Food:', options)