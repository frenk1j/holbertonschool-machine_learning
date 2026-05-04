#!/usr/bin/env python3
"""Task 1: Create the Q&A input loop"""

if __name__ == '__main__':
    while True:
        # Prompt user for input
        question = input("Q: ")

        # Check for exit keywords (case insensitive)
        if question.strip().lower() in ['exit', 'quit', 'goodbye', 'bye']:
            print("A: Goodbye")
            break

        # Print empty answer placeholder
        print("A:")
