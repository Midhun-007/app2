import streamlit as s
import pandas as p
s.set_page_config(layout='wide')
s.title('Free Fire Friends')
col1,col2,col3=s.columns([1.5,0.5,1.5])
a=p.read_csv(r'C:\Users\Midhun.S\PycharmProjects\app-2\selfcoding\ff.csv')
with col1:
    for index,row in a[:4].iterrows():
        s.header(row['name'])
        s.subheader(row['skill'])
with col3:
    for index,row in a[4:].iterrows():
        s.header(row['name'])
        s.subheader(row['skill'])