#!/usr/bin/env python3
"""Convert a gensim Word2Vec model to a Keras Embedding layer"""
import numpy as np
from keras.layers import Embedding


def gensim_to_keras(model):
    """Converts a gensim word2vec model to a trainable Keras Embedding layer"""
    weights = model.wv.vectors
    vocab_size, vector_size = weights.shape
    embedding = Embedding(
        input_dim=vocab_size,
        output_dim=vector_size,
        weights=[weights],
        trainable=True
    )
    return embedding
