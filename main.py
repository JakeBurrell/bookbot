import sys
from stats import count_words, count_letters, sort_count_letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_name = sys.argv[1]
    text = get_book_text(file_name)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    letter_dict = count_letters(text)
    letter_dict = sort_count_letters(letter_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("---------Word Count------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in letter_dict:
        print(f"{item['letter']}: {item['num']}")

def get_book_text(file):
    text = ""
    with open(file) as f:
        text = f.read()
    return text


main()
