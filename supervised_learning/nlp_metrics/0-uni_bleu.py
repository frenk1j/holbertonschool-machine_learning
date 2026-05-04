#!/usr/bin/env python3
"""Task 0: Unigram BLEU score"""
import numpy as np


def uni_bleu(references, sentence):
    """
    Calculates the unigram BLEU score for a sentence.

    Args:
        references: list of reference translations (each is a list of words)
        sentence: list of words in the proposed sentence

    Returns:
        the unigram BLEU score
    """
    # Count occurrences of each word in the sentence
    sentence_counts = {}
    for word in sentence:
        sentence_counts[word] = sentence_counts.get(word, 0) + 1

    # Clipped count: for each word, take min(sentence_count, max_ref_count)
    clipped_count = 0
    for word, count in sentence_counts.items():
        # Find max count of this word across all references
        max_ref_count = max(
            ref.count(word) for ref in references
        )
        clipped_count += min(count, max_ref_count)

    # Precision = clipped_count / len(sentence)
    precision = clipped_count / len(sentence)

    # Brevity penalty
    # Find the reference length closest to the sentence length
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
