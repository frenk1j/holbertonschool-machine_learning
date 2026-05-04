#!/usr/bin/env python3
"""Task 2: Answer Questions from a reference text"""
question_answer = __import__('0-qa').question_answer


def answer_loop(reference):
    """
    Answers questions from a reference text in an interactive loop.

    Args:
        reference: the reference text to search for answers
    """
    while True:
        # Prompt user for input
        question = input("Q: ")

        # Check for exit keywords (case insensitive)
        if question.strip().lower() in ['exit', 'quit', 'goodbye', 'bye']:
            print("A: Goodbye")
            break

        # Try to find answer in reference text
        answer = question_answer(question, reference)

        if answer is None or not answer.strip():
            print("A: Sorry, I do not understand your question.")
        else:
            print("A: {}".format(answer))
