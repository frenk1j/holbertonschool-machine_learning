#!/usr/bin/env python3
"""Task 3: Semantic Search on a corpus of documents"""
import os
import numpy as np
import tensorflow_hub as hub


def semantic_search(corpus_path, sentence):
    """
    Performs semantic search on a corpus of documents.

    Args:
        corpus_path: path to the corpus of reference documents
        sentence: the sentence from which to perform semantic search

    Returns:
        the reference text of the document most similar to sentence
    """
    # Load Universal Sentence Encoder
    model = hub.load(
        "https://tfhub.dev/google/universal-sentence-encoder-large/5"
    )

    # Load all documents from corpus
    documents = []
    doc_texts = []

    for filename in sorted(os.listdir(corpus_path)):
        if filename.endswith('.md'):
            filepath = os.path.join(corpus_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            documents.append(text)
            doc_texts.append(text)

    # Encode the query sentence
    query_embedding = model([sentence])[0].numpy()

    # Encode all documents
    doc_embeddings = model(documents).numpy()

    # Compute cosine similarities
    # Normalize embeddings
    query_norm = query_embedding / np.linalg.norm(query_embedding)
    doc_norms = doc_embeddings / np.linalg.norm(
        doc_embeddings, axis=1, keepdims=True
    )

    # Dot product gives cosine similarity for normalized vectors
    similarities = np.dot(doc_norms, query_norm)

    # Find most similar document
    best_idx = np.argmax(similarities)

    return doc_texts[best_idx]
