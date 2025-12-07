"""Train a simple TF-IDF + LogisticRegression pipeline and save artifacts."""
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from src.preprocess import clean_text

def load_data(path):
    df = pd.read_excel(path)
    # keep only required columns if present
    if 'review' not in df.columns:
        raise ValueError('Dataset must contain a "review" column.')
    # simple label mapping from rating to sentiment if rating exists
    if 'rating' in df.columns:
        def rating_to_sent(r):
            try:
                r = float(r)
            except:
                return 'neutral'
            if r <= 2:
                return 'negative'
            elif r >= 4:
                return 'positive'
            else:
                return 'neutral'
        df['sentiment'] = df['rating'].apply(rating_to_sent)
    elif 'sentiment' not in df.columns:
        raise ValueError('Dataset must contain "rating" or "sentiment" column.')
    df['review_clean'] = df['review'].fillna('').astype(str).apply(clean_text)
    return df

def main(args):
    df = load_data(args.data_path)
    X = df['review_clean']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=10000, ngram_range=(1,2))),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print('Classification report:\n', classification_report(y_test, preds))
    print('Confusion matrix:\n', confusion_matrix(y_test, preds))
    os.makedirs(args.artifact_dir, exist_ok=True)
    joblib.dump(pipe, os.path.join(args.artifact_dir, 'sentiment_pipeline.joblib'))
    print('Saved pipeline to', os.path.join(args.artifact_dir, 'sentiment_pipeline.joblib'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--artifact_dir', type=str, default='artifacts')
    args = parser.parse_args()
    main(args)
