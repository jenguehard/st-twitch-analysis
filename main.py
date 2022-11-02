import pandas as pd
import schedule
import streamlit as st
import os
from utils_func import get_wordcloud
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Scrap Twitch")

df = pd.read_csv("data.csv")
df['date']= pd.to_datetime(df['date'])

fig = px.line(df.resample('T', on='date').message.count().to_frame().reset_index(), x='date', y='message', title='Nombre de message par minutes')
fig.update_xaxes(rangeslider_visible=True)
st.plotly_chart(fig)


fig = px.bar(df.user.value_counts().to_frame().reset_index().head(15), x='index', y='user', title="Users les plus actifs")
st.plotly_chart(fig)

st.title("Référence Sponsors")

fig = px.bar(df[['orange', 'michelin', 'ekwateur', 'nzxt', 'chupa chups', 'logitech', 'redbull', 'direct assurance', 'samsung']].sum().to_frame().reset_index(), x='index', y=0, title="Références au sponsor")
st.plotly_chart(fig)

st.title("Wordcloud")

wordcloud = get_wordcloud(df, "message")

fig, ax = plt.subplots(figsize = (12, 8))
ax.imshow(wordcloud)
plt.axis("off")
st.pyplot(fig)
