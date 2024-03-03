import json
from tokenizer import RegexTokenizer

# Load the documents from the JSON file
with open('wiki_small.json') as f:
    data = json.load(f)

# Create a RegexTokenizer object
tokenizer = RegexTokenizer()

# Tokenize each document's text
for document in data:
    text = document['init_text']
    tokens = tokenizer.tokenize(text)
    print(tokens)
