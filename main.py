from stats import word_counter, merger, character_counter, sorter
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
path = str(sys.argv[1])

def get_book_text(path):
    with open(path) as f:
        frankenstein_contents = f.read()
        return frankenstein_contents
    
def main():
    words = (get_book_text(path).split())
    return words
    
def final_count():
    print(f"Found {word_counter(main())} total words")

new_list = merger(character_counter(path))
new_list.sort(reverse = True, key = sorter)

def layout():
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("\n----------- Word Count ----------")
    final_count()
    print("\n--------- Character Count -------")
    for key in new_list:
        print(f"{key["char"]}: {key["num"]}")

layout()