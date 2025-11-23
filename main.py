import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character counts
    print("--------- Character Count -------")
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    # print each character: count (only alphabetical characters were included)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()