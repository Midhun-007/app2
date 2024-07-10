import streamlit as s
s.set_page_config(layout='wide')
col1,col2=s.columns(2)
with col1:
    s.image('images/photo.png')
with col2:
    s.title('Midhun')
    content="""Hi i am midhun
    These are my projects"""
    s.write(content)#we can use info method to present it more good