def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    return get_book_text("books/frankenstein.txt")


def get_num_words():
    characters = main().split()
    return len(characters)


words = get_num_words()
# print(f"Found {words} total words")


def get_num_characters():
    lower = list(main().lower())

    num_chars = {}
    for char in lower:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars


print(get_num_characters())
