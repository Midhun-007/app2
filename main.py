'''import streamlit as s
import pandas as p
s.set_page_config(layout='wide')
col1,col2=s.columns(2)
with col1:
    s.image('images/img.png')
with col2:
    s.title('Midhun')
    content="Hi i am midhun
    These are my projects"
    s.write(content)#we can use info method to present it more good

a=p.read_csv('data.csv',sep=';')
#col3,col4,col5=s.columns(3)# col4 has no value thus it assign empty column
#instead of above code which assign same column width for three columns u could use
col3,col4,col5=s.columns([1.5,0.5,1.5])
with col3:
    for index,row in a[:10].iterrows():
        s.header(row['title'])#if we use title instead of header then font size
        #is big like this s.title(row['title'])
        s.write(row['description'])
        s.image('images/'+row['image'])
        #s.write(['Source code'](row['url'])) This return =s error as we dont use f sring
        s.write(f"[Source code]({row['url']})")#see this syntax carefully 214 video
with col5:
    for index,row in a[10:].iterrows():
        s.header(row['title'])
        s.write(row['description'])
        s.image('images/'+row['image'])
        s.write(f"[Source code]({row['url']})")'''
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
