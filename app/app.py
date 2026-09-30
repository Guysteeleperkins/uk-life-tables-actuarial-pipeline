import streamlit as st
from db_queries import get_life_expectancy
import plotly.express as px

st.title("UK Life Expectancy Explorer")

sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 30)

data = get_life_expectancy(sex, age)
fig = px.line(data, x="time_period", y="ex")
fig.update_xaxes(type="category")  # treats years as labels, not numbers, so no comma formatting
st.plotly_chart(fig)
