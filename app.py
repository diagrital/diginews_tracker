# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:24:28 2023

@author: aspirex99
"""
import streamlit as st
import pandas as pd
#st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  df = df[df['Pulse'] == 0]
  df = df[["Name", "Phone Number", "Speaker"]]
  #df = pd.read_csv("dir/file.csv")
  @st.experimental_memo
  def convert_df(df):
      return df.to_csv(index=False).encode('utf-8')
  csv = convert_df(df)
  st.download_button("Press to Download",csv,"file.csv","text/csv",
  key='download-csv')
  #print(df.head())
  #st.write(df.head())