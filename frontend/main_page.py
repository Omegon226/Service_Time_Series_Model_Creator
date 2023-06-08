import streamlit as st

st.title("ABOBA")

option = st.selectbox("aboba?", ("YES", "Hmm", "No"))
st.write("")
x = st.slider("X", 0, 100, 20)
y = st.slider("X", 0, 130, 10)

inputs = {"operation": option, "x": x, "y": y}

if st.button("Calculate"):
    st.subheader(f"Response from ABOBA = {str(x + y)}")
