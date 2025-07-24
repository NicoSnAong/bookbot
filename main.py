import sys
from stats import count_words, count_caracters, dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as book:
        return book.read()

def main(book_path):
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    total_words = count_words(text)
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    char_dict = count_caracters(text)
    sorted_chars = dict_to_sorted_list(char_dict)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # (Optionnel mais mieux) attraper l'erreur si le fichier n'existe pas
    try:
        main(book_path)
    except FileNotFoundError:
        print(f"Error: file '{book_path}' not found.")
        sys.exit(1)

