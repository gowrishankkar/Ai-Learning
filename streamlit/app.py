import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hello new data")
st.write("This is a sample Streamlit app.")


df = pd.DataFrame({
    'first coulumn': [1, 2, 3, 4],
    'second coulumn': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.dataframe(df)

## create line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)   
st.line_chart(chart_data)