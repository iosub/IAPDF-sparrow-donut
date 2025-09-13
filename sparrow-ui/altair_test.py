import streamlit as st
import altair as alt
import pandas as pd

df = pd.DataFrame({'Status': ['A', 'B'], 'Value': [10, 20]})
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Value:Q'),
    y=alt.Y('Status:N', sort='-x'),
    color=alt.Color('Status:N')
)
st.altair_chart(chart)
