from stats import count_words
from stats import count_caracters

def get_book_text(path_to_file):
    with open(path_to_file) as book :
        text=book.read()
    return text

def main():
    text=get_book_text("./books/frankenstein.txt")
    print(f"{count_words(text)} words found in the document")
    print(count_caracters(text))
    

main() 