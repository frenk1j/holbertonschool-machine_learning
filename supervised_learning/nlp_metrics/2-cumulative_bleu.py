#!/usr/bin/env python3
"""Task 2: Cumulative N-gram BLEU score"""
import numpy as np


def cumulative_bleu(references, sentence, n):
    """
    Calculates the cumulative n-gram BLEU score for a sentence.

    Args:
        references: list of reference translations (each is a list of words)
        sentence: list of words in the proposed sentence
        n: size of the largest n-gram to use for evaluation

    Returns:
        the cumulative n-gram BLEU score
    """
    def get_ngrams(words, k):
        """Returns a dict of k-gram counts from a list of words."""
        ngrams = {}
        for i in range(len(words) - k + 1):
            gram = tuple(words[i:i + k])
            ngrams[gram] = ngrams.get(gram, 0) + 1
        return ngrams

    # Compute precision for each n-gram order 1..n
    precisions = []
    for k in range(1, n + 1):
        sentence_ngrams = get_ngrams(sentence, k)
        total = sum(sentence_ngrams.values())

        if total == 0:
            precisions.append(0.0)
            continue

        clipped_count = 0
        for gram, count in sentence_ngrams.items():
            max_ref_count = max(
                get_ngrams(ref, k).get(gram, 0) for ref in references
            )
            clipped_count += min(count, max_ref_count)

        precisions.append(clipped_count / total)

    # Weighted geometric mean with uniform weights (1/n each)
    # log of geometric mean = (1/n) * sum(log(p_k))
    weights = [1 / n] * n

    # If any precision is 0, BLEU is 0
    if any(p == 0 for p in precisions):
        bleu = 0.0
    else:
        log_avg = sum(w * np.log(p) for w, p in zip(weights, precisions))
        bleu = np.exp(log_avg)

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

    return bp * bleu
