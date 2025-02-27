# News Summarizer and QA Bot

## Overview
This project consists of two implementations:
1. **Code Version:** A Python script that extracts text from news articles, generates a summary, and answers user questions based on the article content.
2. **Streamlit Version:** A web-based interface that allows users to enter multiple news article URLs, view summaries in a tabular format, and ask questions interactively.

## Features
- Extracts article content from URLs.
- Generates summaries using a frequency-based approach.
- Allows users to input multiple articles.
- Provides a QA bot that answers questions based on specific articles.
- Streamlit UI for easy interaction.

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install newspaper3k pandas nltk transformers streamlit
```
Additionally, download the necessary NLTK resources:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Usage
### 1. Running the Code Version
Execute the script using:
```sh
python article_review.py
```
This version will prompt for URLs and questions in a terminal environment.

### 2. Running the Streamlit Version (Local Deployment)
Start the Streamlit app by running:
```sh
streamlit run streamlit.py
```
Then, open the provided local URL in your web browser to use the interactive UI.

## How to Use the Streamlit App
1. Enter multiple news article URLs (one per line) in the text area.
2. Click **Add Articles** to fetch and summarize them.
3. View the summaries in a table.
4. Ask a question in the format: `Article X: Your question` (e.g., `Article 1: What is the main topic?`).
5. Click **Get Answer** to receive an AI-generated response.

## Notes
- Fetching and summarizing articles may take some time; a spinner is displayed during processing.
- Ensure a stable internet connection for retrieving article content.

## Future Enhancements
- Improve summary generation using advanced NLP models.
- Add support for summarizing uploaded text files.
- Extend the QA model to support multilingual queries.


