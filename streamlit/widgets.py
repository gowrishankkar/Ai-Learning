import streamlit as st
import pandas as pd

st.title("Hello new data")
st.write("This is a sample Streamlit app.")

name=st.text_input("Enter your name", "Type here...")

if name:
    st.write(f"Hello, {name}!")


age=st.slider("Select your age", 0, 100, 25)

st.write(f"You are {age} years old.")

options = ['Python', 'JavaScript', 'C++', 'Java', 'Go']
choice = st.selectbox("Select your favorite programming language", options)
st.write(f"You selected: {choice}")



data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
st.write("Here's a sample DataFrame:", df)

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Here's the data from your uploaded file:", uploaded_df)