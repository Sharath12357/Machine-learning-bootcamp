import streamlit as st
import pandas as pd

st.write("Welcomw to textboxlibe printing message")

name=st.text_input("Enter your name ")
if name:

    st.write(f"Hello { name } welcome to the mall")