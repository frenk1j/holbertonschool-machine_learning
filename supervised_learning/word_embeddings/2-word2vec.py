#!/usr/bin/env python3
"""Train a gensim Word2Vec model."""
import gensim


def word2vec_model(sentences, vector_size=100, min_count=5, window=5,
                   cbow=True, epochs=5, seed=0, workers=1):
    """Create and return a trained Word2Vec model."""
    
    sg = 0 if cbow else 1
    
    model = gensim.models.Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg,
        epochs=epochs,
        seed=seed,
        workers=workers
    )
    
    return model