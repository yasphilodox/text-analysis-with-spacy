# Text Analysis with spaCy
This project demonstrates a basic implementation of text processing using the spaCy library. The code processes a text file, filters tokens based on stopwords, punctuation, and specific parts of speech, and then counts the occurrence of each lemma in the text.

## Features
- Tokenization: Processes each line of text using spaCy’s nlp pipeline.
- Stopword Removal: Removes standard stopwords and punctuation from the token list.
- POS Filtering: Filters out pronouns and verbs.
- Lemma Extraction: Extracts the lemmas of the filtered tokens.
- Word Frequency Counting: Counts the frequency of each lemma and displays the most frequent lemmas in descending order.
## Requirements
- Python 3.x
- spaCy (en_core_web_sm model)
- To install the necessary packages, run:
pip install spacy
python -m spacy download en_core_web_sm
