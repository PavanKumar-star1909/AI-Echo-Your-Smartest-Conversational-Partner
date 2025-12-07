# AI Echo: Your Smartest Conversational Partner

Minimal project scaffold for sentiment analysis on ChatGPT-style reviews.

## Structure
- data/ - place `chatgpt_style_reviews_dataset.xlsx` here
- src/ - preprocessing, training, prediction modules
- app.py - Streamlit app to demo predictions
- requirements.txt - Python packages
- README.md - this file

## Quickstart
1. Create a Python virtual environment and activate it.
2. Install requirements: `pip install -r requirements.txt`
3. Put your dataset `chatgpt_style_reviews_dataset.xlsx` inside the `data/` folder.
4. Train a model: `python src/train.py --data_path data/chatgpt_style_reviews_dataset.xlsx`
5. Run the app: `streamlit run app.py`

## Notes
This is a simple, easy-to-follow template. Extend models, EDA, and deployment as needed.
