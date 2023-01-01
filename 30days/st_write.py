import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
#Example 
st.write('Hello *World!* :sunglasses:')

#Example 2
st.write (1234)

#example 3
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column': [10,5,6,8]
})

st.write(df)

#Example 4
st.write('Below is DataFrame:', df, 'Above is dataframe')

#Example 5
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c'])
st.write(c)