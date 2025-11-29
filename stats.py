import sys

if len(sys.argv) == 2:
    book = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    return get_book_text(book)


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


# print(get_num_characters())


def sort_on(items):
    return items["num"]


def sorted_chars():
    unsorted = get_num_characters()
    unsorted_list = []
    for char in unsorted:
        num = unsorted[char]
        temp_dict = {"char": char, "num": num}
        if char.isalpha():
            unsorted_list.append(temp_dict)

    unsorted_list.sort(key=sort_on, reverse=True)
    return unsorted_list
