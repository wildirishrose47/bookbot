import sys

from stats import get_num_words, sorted_chars

if len(sys.argv) == 2:
    path_to_book = sys.argv[1]
    words = get_num_words()
    sorted_list = sorted_chars()
    print(
        f"============ BOOKBOT ============\nAnalyzing book found at {path_to_book}...\n----------- Word Count ----------\nFound {words} total words\n----------- Character Count ----------\n"
    )
    for char in sorted_chars():
        print(f"{char['char']}: {char['num']}")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
