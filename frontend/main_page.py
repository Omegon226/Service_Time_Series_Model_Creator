import streamlit as st
import requests

st.markdown("""
    # Hello, :a::b::o2::b::a:
    """)


x = requests.get("http://127.0.0.1:8000/data_manipulation/get_all_params_of_time_series/")
a = x.text
b = x.content
c = x.json()

st.text(x.json())
