import streamlit as st
from textblob import TextBlob
from textblob import Word
def get_all_nouns(blob):
    nouns = []
    for tag in blob.tags:
        if tag[1] == 'NN':
            nouns.append(tag[0])
    return nouns 

def get_sentiment(blob):
    polarity = blob.sentiment.polarity
    if polarity < 0:
        return 'negative'
    elif polarity ==0:
        return "netural"
    else:
        return 'positive'  

def spell_check(text):
    words = text.split()
    output = {}
    for word in words:
        output[word]=Word(word).spellcheck()[0][1]
    return output    



st.sidebar.title('NLP using TextBlob')
msg = st.text_area('Enter something in English',height=300)
if st.button('Update'):

    st.sidebar.subheader('Your content')
    st.sidebar.write(msg)
if msg:
    blob = TextBlob(msg)
    st.subheader('part of speech Tagging: Nouns')
    st.write(get_all_nouns(blob))  

    st.subheader('Sentiment Analysis ')
    st.info(get_sentiment(blob))

    st.subheader('Check spelling')
    st.write(spell_check(msg))
    st.success(blob.correct())