import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
import newspaper

def extract_text(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text

def frequency_based_summary(text, num_sentences=3):
    nltk.download('stopwords')
    nltk.download('punkt')
    
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(re.sub(r'[^a-zA-Z]', ' ', text.lower()))
    
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    word_frequencies = Counter(words)
    sentence_scores = {sent: sum(word_frequencies[word] for word in nltk.word_tokenize(sent.lower()) if word in word_frequencies) for sent in sentences}
    
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return " ".join(summary_sentences)

def answer_question(context, question):
    from transformers import pipeline
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    answer = qa_pipeline(question=question, context=context)
    return answer['answer']

if __name__ == "__main__":
    articles = {}
    while True:
        url = input("Enter news article URL (or type 'done' to finish): ")
        if url.lower() == 'done':
            break
        text = extract_text(url)
        summary = frequency_based_summary(text)
        articles[url] = {'text': text, 'summary': summary}
    
    # Display summaries in a table
    df = pd.DataFrame([{"Article": f"Article {i+1}", "Summary": data['summary']} for i, (url, data) in enumerate(articles.items())])
    print("\nSummaries:")
    print(df.to_string(index=False))
    
    while True:
        question = input("\nAsk a question (format: 'Article X: Your question' or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        
        try:
            article_num, user_question = question.split(':', 1)
            article_index = int(article_num.strip().split()[-1]) - 1
            
            if article_index < 0 or article_index >= len(articles):
                print("Invalid article number. Try again.")
                continue
            
            context = list(articles.values())[article_index]['text']
            answer = answer_question(context, user_question.strip())
            print("Answer:", answer)
        except Exception as e:
            print("Invalid format. Use 'Article X: Your question'")