import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from datetime import time,datetime

st.header("Practice Streamlit")

st.write("Hello, *World!* :sunglasses:")

# st.header("st.button")
#
# if st.button("Say hello"):
#     st.write("Why hello there")
# else:
#     st.write("Goodbye")

st.write(1234)

df = pd.DataFrame({
    "first_column": [1, 2, 3, 4],
    "second_column": [10, 20, 30, 40]
})

st.write(df)

st.write("Below is a DataFrame:", df, "above is a dataframe")

df2 = pd.DataFrame(
    np.random.randn(200, 3), #200行3列的随机数据
    columns=['a', 'b', 'c'])

c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c'])

st.write(c)


