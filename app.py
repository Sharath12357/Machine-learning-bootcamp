import streamlit as st
import pandas as pd
import numpy as  np

st.title("Hello Streamlit")

st.write("Hello This is a Sample text data to shown you")

chart_data=pd.DataFrame(
    {"name":"sharath","age":21},
    {"name":"Chaithra","age":21}
)
st.write(chart_data)


data=pd.DataFrame(
    np.random.randn(20,3),columns=['A','B','C']
)
st.line_chart(data)