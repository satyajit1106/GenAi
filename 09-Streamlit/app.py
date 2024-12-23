import streamlit as st
import pandas as pd
import numpy as np

# title of the application
st.title("hello streamlit")

# display a simple text
st.write("this is the simple text")

# create the simple data frame
df = pd.DataFrame({
    'first column':[1,2,3],
    'second column': [4,5,6]
})

# display the data frame
st.write("here is the dataframe")
st.write(df)

# create the line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

