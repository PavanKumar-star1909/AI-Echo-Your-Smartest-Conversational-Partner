"""Streamlit demo app for AI Echo sentiment prediction."""
import streamlit as st
from src.preprocess import clean_text
from src.predict import load_pipeline, predict
import os

st.set_page_config(page_title='AI Echo - Sentiment Demo', layout='centered')

st.title('AI Echo — Sentiment Analyzer')
st.markdown('Upload `chatgpt_style_reviews_dataset.xlsx` and/or enter text to see predicted sentiment.')

col1, col2 = st.columns([2,1])

with col1:
    user_text = st.text_area('Enter a review to classify', height=180)
    if st.button('Predict'):
        pipeline_path = os.path.join('artifacts','sentiment_pipeline.joblib')
        if not os.path.exists(pipeline_path):
            st.error('No trained model found. Run training: `python src/train.py --data_path data/chatgpt_style_reviews_dataset.xlsx`')
        else:
            pipe = load_pipeline(pipeline_path)
            cleaned = clean_text(user_text)
            pred = pipe.predict([cleaned])[0]
            st.success(f'Predicted sentiment: **{pred}**')

with col2:
    st.write('Actions')
    if st.button('Show README'):
        st.write(open('README.md').read())

st.sidebar.header('About')
st.sidebar.markdown('This is a minimal demo scaffold. Train a model with your data and use this app to demo predictions.')
