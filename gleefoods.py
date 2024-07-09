
import streamlit as st
import pandas as pd
import altair as alt

# Load dataset (replace with your own data)
data = pd.read_csv("your_data.csv")

# Create Streamlit app
st.title("Data Visualization App")

# Select column to visualize
column = st.selectbox("Choose a column", data.columns)

# Create bar chart using Altair
chart = alt.Chart(data).mark_bar().encode(x="index", y=column)

# Display chart
st.altair_chart(chart, use_container_width=True)
```
This app uses:

- Streamlit (st) for the app framework
- Pandas (pd) to load the dataset
- Altair (alt) for data visualization
'''