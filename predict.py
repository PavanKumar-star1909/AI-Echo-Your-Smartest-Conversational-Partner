"""Utility to load the trained pipeline and predict sentiment for new texts."""
import joblib
from typing import List

def load_pipeline(path='artifacts/sentiment_pipeline.joblib'):
    return joblib.load(path)

def predict(texts, pipeline=None):
    if pipeline is None:
        pipeline = load_pipeline()
    return pipeline.predict(texts)
