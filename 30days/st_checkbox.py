#st.checkbox display checkbox widget
import streamlit as st

st.header('Learn st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Great! Here's some more ☕")

if cola:
    st.write("Great! Here's some more 🥤")
    