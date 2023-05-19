from collections import Counter
import json
from typing import List
from indexing_process import TransformedDocumentCollection


def get_best_terms(transformed_docs, stopwords):
    best_terms = []
    for doc in transformed_docs.get_all_docs():
        counter = Counter()
        counter.update(doc.tokens)
        for stopword in stopwords:
            del counter[stopword]
        best_terms.append(counter.most_common(10))
    with open('best_terms.json', 'w') as f:
        json.dump(best_terms, f)
    return best_terms