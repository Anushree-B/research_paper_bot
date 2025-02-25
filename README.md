# Research Paper Review and Q&A Bot

## Overview
This project extracts text from research papers in PDF format, summarizes key sections, and provides structured reviews. Additionally, it includes a Question-Answering (QA) bot that answers queries based on the extracted text.

## Features
- Extracts text from PDF research papers.
- Summarizes the research paper using NLP techniques.
- Identifies key sections such as **Introduction, Methodology, Results, and Conclusion**.
- Extracts **keywords** from the text.
- Provides an automated **review** of the paper.
- Answers user queries based on the research paper content using a transformer-based model.

## Dependencies
Make sure you have the following Python libraries installed:
```bash
pip install PyPDF2 spacy gensim transformers
```
Additionally, download the required SpaCy model:
```bash
python -m spacy download en_core_web_sm
```

## Usage
### 1. Extract and Review a Research Paper
Run the following command to analyze a research paper:
```bash
python research_review.py
```
Make sure to replace `sample_paper.pdf` with your actual PDF file.

### 2. Ask Questions About the Paper
Modify the `question` variable in the script to ask questions about the content:
```python
question = "What is the main contribution of this research?"
```
Run the script to get an answer based on the extracted text.

## Example Output
```
Research Paper Review
=====================

Keywords: deep learning, image processing, classification

Summary:
This paper explores the application of deep learning in image classification...

Section-wise Analysis:
- Introduction: Discusses the background and motivation...
- Methodology: Explains the dataset and model used...
- Results: Shows experimental findings and comparisons...
- Conclusion: Summarizes key contributions and future work...

Q: What is the main contribution of this research?
A: The research introduces a novel deep learning model for improved accuracy...
```

## Contributions
Feel free to fork this repository and submit pull requests for improvements!


