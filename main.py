import pandas as pd
import schedule
import streamlit as st
import os
from utils_func import get_wordcloud
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Scrap Twitch")

df = pd.read_csv("data.csv")
print(df)
print(df.dtypes)
fig = px.line(df.resample('T', on='date').message.count().to_frame().reset_index(), x='date', y='message', title='Time Series with Rangeslider')

fig.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig)

