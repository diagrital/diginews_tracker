# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:24:28 2023

@author: aspirex99
"""
import streamlit as st
import pandas as pd
import os
#st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")




if uploaded_file is not None:
  file_name = uploaded_file.name
  df = pd.read_excel(uploaded_file)
  #cols = st.sidebar.selectbox("Number of columns you want in your data", list(range(len(df.columns))), index=0)
  pulse_value = st.sidebar.selectbox("Select pulse", [0,1,2,3,4,5], index=0)
  pulse_value_2 = st.sidebar.selectbox("Select pulse 2",[0,1,2,3,4,5],index = 0)
  df = df[(df['Pulse'] == pulse_value) | (df['Pulse'] == pulse_value_2)]
  df = df[["Name", "Phone Number", "Speaker",'Pulse']]
  df['Speaker'] = df['Speaker'].replace(['Yes','No'], [1,0])
  #st.table(df[["Name", "Phone Number", "Speaker",'Pulse']])
  
  df = df[["Name", "Phone Number", "Speaker"]].reset_index(drop = True)
  @st.experimental_memo
  
  #df = pd.read_csv("dir/file.csv")
  
  @st.experimental_memo
  st.write(df)
  def convert_df(df):
      return df.to_excel(index=False)
  csv = convert_df(df)
  st.download_button("Press to Download",df.to_excel('file.xlsx',index=False),"file.csv","text/csv",
  key='download-file')
  #print(df.head())
  #st.write(df.head())
