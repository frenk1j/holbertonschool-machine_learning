#!/usr/bin/env python3
"""Task 1: N-gram BLEU score"""
import numpy as np


def ngram_bleu(references, sentence, n):
    """
    Calculates the n-gram BLEU score for a sentence.

    Args:
        references: list of reference translations (each is a list of words)
        sentence: list of words in the proposed sentence
        n: size of the n-gram to use for evaluation

    Returns:
        the n-gram BLEU score
    """
    def get_ngrams(words, n):
        """Returns a dict of n-gram counts from a list of words."""
        ngrams = {}
        for i in range(len(words) - n + 1):
            gram = tuple(words[i:i + n])
            ngrams[gram] = ngrams.get(gram, 0) + 1
        return ngrams

    # Get n-grams from sentence
    sentence_ngrams = get_ngrams(sentence, n)

    # Total number of n-grams in sentence
    total = sum(sentence_ngrams.values())

    if total == 0:
        return 0.0

    # Clipped count
    clipped_count = 0
    for gram, count in sentence_ngrams.items():
        # Max count of this n-gram across all references
        max_ref_count = max(
            get_ngrams(ref, n).get(gram, 0) for ref in references
        )
        clipped_count += min(count, max_ref_count)

    # Precision
    precision = clipped_count / total

    # Brevity penalty
    sentence_len = len(sentence)
    ref_lengths = [len(ref) for ref in references]
    closest_ref_len = min(
        ref_lengths,
        key=lambda ref_len: (abs(ref_len - sentence_len), ref_len)
    )

    if sentence_len >= closest_ref_len:
        bp = 1.0
    else:
        bp = np.exp(1 - closest_ref_len / sentence_len)

    return bp * precision
