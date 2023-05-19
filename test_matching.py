from unittest import TestCase
from matching import *


class Test(TestCase):
    def test_search(self):
        self.assertEqual(['red and yellow'],
                         search('red', ['red and yellow', 'blue and yellow', 'predict color']))

    def test_string_match__matches(self):
        self.assertTrue(string_match('red', 'red and yellow'))

    def test_string_match__dont_match(self):
        self.assertFalse(string_match('red', 'yellow and blue'))

    def test_string_match__match_substring(self):
        self.assertTrue(string_match('red', 'predict color'))

#Search
    #Empty string as a query
    def test_search__empty_string_query(self):
        self.assertEqual([], search("", ['red and yellow', 'blue and yellow', 'predict color']))

    #Empty string as a document
    def test_search__empty_string_document(self):
        self.assertEqual([], search("red and yellow", ""))

    # Empty document list
    def test_search__empty_document_list(self):
        self.assertEqual([], search("red and yellow", []))

#Boolean Match

    def test_boolean_term_match__matches(self):
        self.assertTrue(string_match('red', 'red and yellow'))

    def test_boolean_term_match__dont_match(self):
        self.assertFalse(string_match('red', 'yellow and blue'))

    def test_boolean_term_match__match_substring(self):
        self.assertTrue(string_match('red', 'predict color'))

    #Empty query
    def test_boolean_term_match__empty_query(self):
        self.assertFalse(boolean_term_match("", "red"))

    #Empty document
    def test_boolean_term_match__empty_document(self):
        self.assertFalse(boolean_term_match("red", ""))

    #Multi Doc
    def test_string_match__multi_document(self):
        self.assertTrue("yellow and red", "red")

#String Match
    #Empty Query
    def test_string_match__empty_query(self):
        self.assertFalse(string_match("", "red"))

    #Empty Doc and doc list (these are the same so i didn't add another one)
    def test_string_match__empty_document(self):
        self.assertFalse(string_match("red", ""))

    #Multi Doc
    def test_string_match__multi_document(self):
        self.assertTrue("yellow and red", "red")

#Search String match unexpected result
    def test_string_match_unexpected_result(self):
        query = 'red'
        document = 'predict color'
        self.assertTrue(string_match(query, document))
        self.assertFalse(search(query, [document]) == document)

#Differentiate string and boolean matching
    def test_matching_function_difference(self):
        self.assertTrue(string_match("red", "[red and yellow]"))
        self.assertFalse(boolean_term_match("red", "[red and yellow]"))

