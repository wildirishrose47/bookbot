from unittest.main import main


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    return get_book_text("books/frankenstein.txt")


def get_num_words():
    return len(main().split())


words = get_num_words()
print(f"Found {words} total words")
