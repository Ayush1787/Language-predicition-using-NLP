# Importing the necessary libraries
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pickle


# Load the model
model=pickle.load(open('model.pkl','rb'))
cv=pickle.load(open('Vectorizer.pkl','rb'))


# Title
st.title('Language Prediction App')


# Text Area for user input
text=st.text_area('Enter Text')


# Predict the language
if st.button('Predict Language'):
    array_data=[text]
    vector_data=cv.transform(array_data)
    result=model.predict(vector_data)
    st.success(result)
else:
    st.warning('Please enter some text')