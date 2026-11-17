import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl

df = pd.read_excel("dados-educacao.xlsx")

df_filtrado = df[(df["escolaridade"].isin(["Mestrado"]))
].copy()