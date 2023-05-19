#Rana Hani and Sulaeman Ahmed Text-Processing Group 3
import json
import re
import time
import timeit
import typing


class Tokenizer:
    def tokenize(self, document_text: str) -> typing.List[str]:
        pass


class NaiveTokenizer(Tokenizer):
    def tokenize(self, document_text: str) -> typing.List[str]:
        start_time = timeit.default_timer()
        pattern = document_text.replace('.', ' . ').replace(',', ' , ').lower().split()
        tokens = re.findall(pattern, document_text.lower())
        end_time = timeit.default_timer()
        print(f"NaiveTokenizer execution time: {end_time - start_time} seconds")
        return tokens


class RegexTokenizer(Tokenizer):
    def tokenize(self, text):
        start_time = time.time()
        tokens = re.findall(
            r"\b" # Match a word boundary
            r"(?!https?://)"  # Negative lookahead to exclude URLs starting with "http://" or "https://"
            r"(?<!\.)"  # Negative lookbehind to exclude URLs starting with a dot
            r"\b[\w.]+" # Match one or more word characters or dots. This matches words and numbers that may include decimal points.
            r"(?:'\w+)?" # Optionally match an apostrophe followed by one or more word characters
            r"\b(?!\.\w)" # Negative lookahead to exclude URLs ending with a dot and a word character
            r"|" #or
            r"[^\s\w]+" # Match one or more non-space and non-word characters. This matches punctuation marks like commas and exclamation marks.
            r"|" #or
            r"(?:(?<!://)" # Negative lookbehind to exclude URLs starting with "http://" or "https://"
            r"(?:https?://|www\.)" # Match "http://" or "https://" or "www."
            r"[^\"'\s]+" # Match one or more non-space and non-quote characters after "http://" or "https://" or "www."
            r")", # End non-capturing group for URLs

            #r"\b(?!https?://)(?<!\.)\b[\w.]+(?:'\w+)?\b(?!\.\w)|[^\s\w]+|(?:(?<!://)(?:https?://|www\.)[^\"'\s]+)",
            text.lower())
        end_time = time.time()
        print(f"RegexTokenizer execution time: {end_time - start_time} seconds")
        return tokens


import unittest


class TokenizerTestCase(unittest.TestCase):
    def setUp(self):
        self.naive_tokenizer = NaiveTokenizer()
        self.regex_tokenizer = RegexTokenizer()

    #def test_naive_tokenizer(self):
        # Test basic tokenization
        #self.assertEqual(self.naive_tokenizer.tokenize("Hello, world!"), ['hello', ',', 'world', '!'])

        # Test handling of apostrophes
         #self.assertEqual(self.naive_tokenizer.tokenize("The quick brown fox jumped over the lazy dog's back."), ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', "dog's", 'back', '.'])

        # Test handling where apostrophe should be cut off
         #self.assertEqual(self.regex_tokenizer.tokenize("The company has Denis' car."),['the', 'company', 'has', 'denis', "'", 'car', '.'])

        # Test handling of numbers
         #self.assertEqual(self.naive_tokenizer.tokenize("My favorite number is 3.14."), ['my', 'favorite', 'number', 'is', '3.14', '.'])

        # Test handling of URLs
         #self.assertEqual(self.naive_tokenizer.tokenize("Check out my website: https://www.example.com"), ['check', 'out', 'my', 'website', ':', 'https://www.example.com'])


    def test_regex_tokenizer(self):
        # Test basic tokenization
        self.assertEqual(self.regex_tokenizer.tokenize("Hello, world!"), ['hello', ',', 'world', '!'])

        # Test handling of apostrophes
        self.assertEqual(self.regex_tokenizer.tokenize("The quick brown fox jumped over the lazy dog's back."),
                         ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', "dog's", 'back', '.'])

        #Test handling where apostrophe should be cut off
        self.assertEqual(self.regex_tokenizer.tokenize("The company has Denis' car."),
                         ['the', 'company', 'has', 'denis', "'", 'car', '.'])

        # Test handling of numbers
        self.assertEqual(self.regex_tokenizer.tokenize("My favorite number is 3.14."),
                         ['my', 'favorite', 'number', 'is', '3.14', '.'])

        # Test handling of URLs
        self.assertEqual(self.regex_tokenizer.tokenize("Check out my website: https://www.example.com"),
                         ['check', 'out', 'my', 'website', ':', 'https://www.example.com'])


if __name__ == '__main__':
    unittest.main()

#Tokenizing wiki_small.json
import json
import documents
import tokenizer

from tokenizer import RegexTokenizer

#Load the documents from the JSON file**
with open('wiki_small.json') as f:
	data = json.load(f)

#Create a RegexTokenizer object**
tokenizer = tokenizer.RegexTokenizer()

#Tokenize each document's text**
for document in data:
	text = document['init_text']
	tokens = tokenizer.tokenize(text)
	print(tokens)