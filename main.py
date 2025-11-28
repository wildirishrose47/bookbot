from unittest.main import main


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    get_book_text(books / frankenstein.txt)


main()
