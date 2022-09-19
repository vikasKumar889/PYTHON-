'''
to run this, open terminal and type
# streamlit run ui/demo1.py
'''
import streamlit as st

st.title('Streamlit Demo')
st.header('Streamlit is awesome')
st.subheader('Its easy to use')
st.text('This is simple text example')
st.write('This is magical function')
st.markdown('This is a **markdown ** example')
st.success('This is success message')
st.info('This is an info message')
st.warning('This is a warning message')
st.error('This is an error message')
st.exception('This is an exception message')



# media element
st.image('20190625_191425.jpg',use_column_width=True)
st.video("https://www.youtube.com/watch?v=pwNZGVHx2hQ")
st.audio('')

# widgets
name = st.text_input('Enter the name')
cost = st.number_input('Enter the cost')
comment = st.text_area("Enter remarks")
status = st.checkbox('save this data')
gender = st.radio('Gender',['Male','Female','Other'])

querylist = ['How to use streamlit?',
            'Is stremlit free or paid?',
            'Is it gonna rain now?']

query = st.selectbox('What the Query',querylist)
rating = st.slider('Select the rating',1,5)
btn = st.button('Submit the response')

# if btn is pressed
if btn:
    st.write('Username:',name)
    st.write('Cost:',cost)
    st.write('Comment:',comment)
    st.write('Status:',status)
    st.write('Gender:',gender)
    st.write('query:',query)
    st.write('rating:',rating)