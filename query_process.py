from typing import List

from documents import DocumentCollection, Document
from index import Index
from tokenizer import NaiveTokenizer
import unittest


class QueryProcess:
    def __init__(self, index: Index, query_transformer, result_formatter):
        self.index = index
        self.query_transformer = query_transformer
        self.result_formatter = result_formatter

    def process_query(self, query: str) -> List[str]:
        return NaiveTokenizer().tokenize(query)

    def format_single_result(self, doc: Document) -> str:
        return doc.text

    def run(self, query: str) -> str:
        processed_query = self.query_transformer(query)
        results = self.index.search(processed_query)
        formatted_results = self.result_formatter.format_results(results)
        return formatted_results

    @staticmethod
    def create_naive_query_process(documents: DocumentCollection, index: Index) -> 'QueryProcess':
        query_transformer = lambda query: NaiveTokenizer().tokenize(query)
        result_formatter = NaiveResultFormatter(documents)
        return QueryProcess(index, query_transformer, result_formatter)


class NaiveResultFormatter:
    def __init__(self, documents: DocumentCollection):
        self.documents = documents

    def format_single_result(self, doc: Document) -> str:
        return doc.text

    def format_results(self, results: List[str]) -> str:
        """
        Given the output of search use documents to create a string to be presented to the user.
        :param results: List of doc_ids
        :return: A single string presented to the user.
        """
        out = ''
        for doc_id in results:
            doc = self.documents.get(doc_id)
            out += '\n' + self.format_single_result(doc)
        return out


class TestNaiveResultFormatter(unittest.TestCase):
    def setUp(self):
        documents = [
            Document('1', 'This is document 1'),
            Document('2', 'hello my people'),
            Document('3', 'This is document 3'),
        ]
        self.document_collection = DocumentCollection(documents)
        self.formatter = NaiveResultFormatter(self.document_collection)

    def test_format_results(self):
        results = ['1', '3']
        expected_output = '\nThis is document 1\nThis is document 3'
        self.assertEqual(self.formatter.format_results(results), expected_output)



