#!/usr/bin/env python3
"""Module for converting a gensim Word2Vec model to a Keras Embedding layer"""
import tensorflow as tf


def gensim_to_keras(model):
    """Converts a gensim word2vec model to a keras Embedding layer.

    Args:
        model: a trained gensim word2vec model

    Returns:
        A trainable keras Embedding layer initialized with the model weights
    """
    # Get the keyed vectors from the model
    keyed_vectors = model.wv

    # Get the weights (word vectors) as a numpy array
    weights = keyed_vectors.vectors

    # vocab size and embedding dimension
    vocab_size, vector_size = weights.shape

    # Create a trainable Keras Embedding layer with the pretrained weights
    embedding_layer = tf.keras.layers.Embedding(
        input_dim=vocab_size,
        output_dim=vector_size,
        weights=[weights],
        trainable=True
    )

    return embedding_layer
