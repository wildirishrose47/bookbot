from unittest.main import main


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    return get_book_text("books/frankenstein.txt")


num_words = len(main().split())


print(f"Found {num_words} total words")
