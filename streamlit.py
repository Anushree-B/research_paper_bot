import re
import nltk
import pandas as pd
import streamlit as st
from nltk.corpus import stopwords
from collections import Counter
import newspaper
from transformers import pipeline
import time

nltk.download('stopwords')
nltk.download('punkt')

st.title("News Summarizer and QA Bot")

def extract_text(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text

def frequency_based_summary(text, num_sentences=3):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(re.sub(r'[^a-zA-Z]', ' ', text.lower()))
    
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    word_frequencies = Counter(words)
    sentence_scores = {sent: sum(word_frequencies[word] for word in nltk.word_tokenize(sent.lower()) if word in word_frequencies) for sent in sentences}
    
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return " ".join(summary_sentences)

def answer_question(context, question):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    return qa_pipeline(question=question, context=context)['answer']

# Store multiple articles
if "articles" not in st.session_state:
    st.session_state.articles = {}

url_input = st.text_input("Enter news article URL")
if st.button("Add Article"):
    if url_input:
        with st.spinner("Fetching and summarizing article..."):
            text = extract_text(url_input)
            summary = frequency_based_summary(text)
            st.session_state.articles[url_input] = {'text': text, 'summary': summary}
        st.success("Article added successfully!")

if st.session_state.articles:
    st.subheader("Summaries")
    df = pd.DataFrame([{"Article": f"Article {i+1}", "Summary": data['summary']} for i, (url, data) in enumerate(st.session_state.articles.items())])
    st.table(df)
    
    st.subheader("Ask a Question")
    question_input = st.text_input("Enter your question (format: 'Article X: Your question')")
    if st.button("Get Answer"):
        try:
            article_num, user_question = question_input.split(':', 1)
            article_index = int(article_num.strip().split()[-1]) - 1
            
            if article_index < 0 or article_index >= len(st.session_state.articles):
                st.error("Invalid article number. Try again.")
            else:
                context = list(st.session_state.articles.values())[article_index]['text']
                with st.spinner("Fetching answer..."):
                    answer = answer_question(context, user_question.strip())
                st.success(f"Answer: {answer}")
        except Exception as e:
            st.error("Invalid format. Use 'Article X: Your question'")
