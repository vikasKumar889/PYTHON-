import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
#import dtale as dt

@st.cache
def load_dataset():
    df =pd.read_excel('ui\Canada.xlsx',
           sheet_name='Canada by Citizenship',
           skiprows=20,
           skipfooter=2)
    return df

# loading the data
Canadasdf = load_dataset()
if st.checkbox('view Raw dataset'):
    st.write(Canadasdf)
