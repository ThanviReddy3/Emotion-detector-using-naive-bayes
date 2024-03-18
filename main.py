import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, r2_score, f1_score, accuracy_score
import pickle

st.header('Emotion detection using ML')
text = st.text_input('Enter the text: ')
model = pickle.load(open(r'C:\Users\india\My Python Files\Machine Learning Phase 2\estimator.pkl', 'rb'))
st.button("submit")
result= model.predict([text])
if result == 'Anger':
    st.image('https://freepngimg.com/thumb/angry_emoji/36886-1-angry-emoji-photo-thumb.png')
elif result == 'Love':
    st.image('https://freepngimg.com/thumb/emoji/64989-emoticon-heart-love-emoji-png-free-photo-thumb.png')
elif result == 'Joy':
    st.image('https://static.vecteezy.com/system/resources/thumbnails/029/138/681/small/happy-emoji-happy-emoji-happy-emoji-transparent-background-ai-generative-free-png.png')
elif result == 'Sad':
    st.image('https://freepngimg.com/thumb/sad_emoji/36860-2-sad-emoji-transparent-image-thumb.png')
elif result == 'Suprise':
    st.image('https://static.vecteezy.com/system/resources/thumbnails/009/665/371/small/emoticon-shocked-face-png.png')
elif result == 'Fear':
    st.image('https://static.vecteezy.com/system/resources/thumbnails/009/885/115/small/fearful-face-emoji-3d-illustration-png.png')