import streamlit as st
from textblob import TextBlob

st.sidebar.title('NLP using TextBlob')
msg = st.text_area('Enter something in English',height=300)
if st.button('Update'):

   st.sidebar.subheader('Your content')
   st.sidebar.write(msg)
if msg:
    blob = TextBlob(msg)
    tags = blob.tags
    st.subheader('Part of Speech Taggin')   
