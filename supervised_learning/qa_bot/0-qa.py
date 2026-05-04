#!/usr/bin/env python3
"""Task 0: Question Answering using BERT"""
import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer


def question_answer(question, reference):
    """
    Finds a snippet of text within a reference document to answer a question.

    Args:
        question: string containing the question to answer
        reference: string containing the reference document

    Returns:
        string containing the answer, or None if no answer found
    """
    # Load pre-trained tokenizer
    tokenizer = BertTokenizer.from_pretrained(
        'bert-large-uncased-whole-word-masking-finetuned-squad'
    )

    # Load BERT QA model from TensorFlow Hub
    model = hub.load("https://tfhub.dev/see--/bert-uncased-tf2-qa/1")

    # Tokenize question and reference
    question_tokens = tokenizer.tokenize(question)
    reference_tokens = tokenizer.tokenize(reference)

    # Build input tokens: [CLS] question [SEP] reference [SEP]
    tokens = (
        ['[CLS]'] + question_tokens +
        ['[SEP]'] + reference_tokens +
        ['[SEP]']
    )

    # Convert tokens to input IDs
    input_word_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Create input mask (all 1s)
    input_mask = [1] * len(input_word_ids)

    # Create input type IDs: 0 for question, 1 for reference
    input_type_ids = (
        [0] * (len(question_tokens) + 2) +
        [1] * (len(reference_tokens) + 1)
    )

    # Convert to tensors and add batch dimension
    input_word_ids_t = tf.expand_dims(
        tf.cast(input_word_ids, tf.int32), axis=0
    )
    input_mask_t = tf.expand_dims(
        tf.cast(input_mask, tf.int32), axis=0
    )
    input_type_ids_t = tf.expand_dims(
        tf.cast(input_type_ids, tf.int32), axis=0
    )

    # Run model
    outputs = model([input_word_ids_t, input_mask_t, input_type_ids_t])

    # Get start and end logits
    start_logits = outputs[0][0]
    end_logits = outputs[1][0]

    # Find the best start and end positions (within reference portion)
    # Reference starts at index len(question_tokens) + 2
    ref_start = len(question_tokens) + 2

    # Get start and end within the reference tokens only
    start_idx = tf.argmax(start_logits[ref_start:-1]).numpy() + ref_start
    end_idx = tf.argmax(end_logits[start_idx:-1]).numpy() + start_idx + 1

    # If start >= end, no valid answer found
    if start_idx >= end_idx:
        return None

    # Extract answer tokens
    answer_tokens = tokens[start_idx: end_idx + 1]

    # Skip if answer is empty or invalid
    if not answer_tokens or answer_tokens == ['[SEP]']:
        return None

    # Convert tokens back to string (handle wordpiece tokens)
    answer = tokenizer.convert_tokens_to_string(answer_tokens)

    if not answer.strip():
        return None

    return answer
