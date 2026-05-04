#!/usr/bin/env python3
"""Task 4: Multi-reference Question Answering"""
qa = __import__('0-qa').question_answer
semantic_search = __import__('3-semantic_search').semantic_search


def question_answer(corpus_path):
    """
    Answers questions from multiple reference texts using semantic search.

    Args:
        corpus_path: path to the corpus of reference documents
    """
    while True:
        # Prompt user for input
        question = input("Q: ")

        # Check for exit keywords (case insensitive)
        if question.strip().lower() in ['exit', 'quit', 'goodbye', 'bye']:
            print("A: Goodbye")
            break

        # Find the most relevant document using semantic search
        reference = semantic_search(corpus_path, question)

        # Try to find answer in the most relevant document
        answer = qa(question, reference)

        if answer is None or not answer.strip():
            print("A: Sorry, I do not understand your question.")
        else:
            print("A: {}".format(answer))
