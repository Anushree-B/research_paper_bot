import PyPDF2
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline
import tf_keras as keras  # Ensures compatibility

import nltk
nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def summarize_text(text, sentences_count=3):
    """Summarizes the given text using sumy LSA summarizer."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)

def analyze_paper(text):
    """Analyzes the research paper and provides a structured review."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    # Extract Keywords
    keywords = {token.text for token in doc if token.is_alpha and not token.is_stop}
    
    # Identify Sections (basic approach)
    sections = {"Introduction": "", "Methodology": "", "Results": "", "Conclusion": ""}
    
    for section in sections.keys():
        if section.lower() in text.lower():
            start = text.lower().find(section.lower())
            end = len(text)
            for next_section in sections.keys():
                if next_section.lower() in text.lower() and text.lower().find(next_section.lower()) > start:
                    end = min(end, text.lower().find(next_section.lower()))
            sections[section] = text[start:end].strip()
    
    # Summarize Sections
    for sec in sections:
        if sections[sec]:
            sections[sec] = summarize_text(sections[sec])

    # **Keywords:** {', '.join(list(keywords)[:10])}
    
    review = f"""
    Research Paper Review
    =====================
    
    
    
    **Summary:**
    {summarize_text(text)}
    
    **Section-wise Analysis:**
    
    - **Introduction:** {sections['Introduction']}
    - **Methodology:** {sections['Methodology']}
    - **Results:** {sections['Results']}
    - **Conclusion:** {sections['Conclusion']}
    """
    
    return review

def answer_question(text, question):
    """Answers a question based on the extracted research paper text using a transformer model."""
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    response = qa_pipeline(question=question, context=text)
    return response['answer']

if __name__ == "__main__":
    pdf_path = "Tiger research paper.pdf"  # Replace with your PDF file path
    #pdf_path = input("Enter the PDF file path: ")
    try:
        text = quit
        (pdf_path)
        review = analyze_paper(text)
        print(review)
        
        while True:
            question = input("Ask a question about the paper (or type 'quit' to exit): ")
            if question.lower() == "quit":
                break
            answer = answer_question(text, question)
            print(f"Q: {question}\nA: {answer}")
    except Exception as e:
        print(f"Error: {e}")
