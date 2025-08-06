import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text (path):
    with open (path) as f:
        text = f.read()
    return text

def main ():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text (file_path)
    
    num_words = get_num_words (book_text)
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words found in the document")

    char_counts = get_char_count(book_text)
    sorted_chars = sort_char_count (char_counts)
 
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main ()