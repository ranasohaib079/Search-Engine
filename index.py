import typing

from documents import TransformedDocument



class Index:
    def add_document(self, doc: TransformedDocument):
        pass

    def search(self, query: typing.List[str]) -> typing.List[str]:
        pass


class NaiveIndex(Index):
    def __init__(self):
        self.docs = dict()

    def add_document(self, doc: TransformedDocument):
        self.docs[doc.doc_id] = set(doc.tokens)

    def search(self, query: typing.List[str]) -> typing.List[str]:
        """
        Does search using the index.
        :param query: List of query terms.
        :return: List of doc_ids for matching documents in correct order.
        """
        query_terms_set = set(query)
        matching_doc_ids = []
        for doc_id, doc_terms_set in self.docs.items():
            if query_terms_set.issubset(doc_terms_set):
                matching_doc_ids.append(doc_id)
        return matching_doc_ids



from collections import defaultdict
import json
from index import Index


class SimpleInvertedIndex(Index):
    def __init__(self):
        self.doc_id_sets = defaultdict(set)

    def add_document(self, doc: TransformedDocument):
        for token in doc.tokens:
            self.doc_id_sets[token].add(doc.doc_id)

    def search(self, query: typing.List[str]) -> typing.List[str]:
        """
        Does search using the index.
        :param query: List of query terms.
        :return: List of doc_ids for matching documents in correct order.
        """
        matching_doc_ids = None
        for term in query:
            doc_ids = self.doc_id_sets[term]
            if matching_doc_ids is None:
                matching_doc_ids = doc_ids
            else:
                matching_doc_ids = matching_doc_ids.intersection(doc_ids)
        return list(matching_doc_ids)

    def write(self, file_path: str):
        data = []
        for key, value in self.doc_id_sets.items():
            data.append({'term': key, 'doc_ids': list(value)})
        with open(file_path, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def read(file_path: str):
        out = SimpleInvertedIndex()
        with open(file_path, 'r') as f:
            data = json.load(f)
            for entry in data:
                out.doc_id_sets[entry['term']] = set(entry['doc_ids'])
        return out
