import sys
from stats import get_num_words

def main():
	if len(sys.argv) != 2:
		print(f"Usage: python 3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	char_count = get_character_count(text)
	sorted_characters = chars_dict_to_sorted_list(char_count)
	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} words found in the document")
	print()

	for item in sorted_characters:
        	if not item["char"].isalpha():
            		continue
        	print(f"{item['char']}: {item['num']}")

	print("--- End report ---")

#Gets Raw Text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Makes Text Lowercase And Counts Characters
def get_character_count(text):
    characters = {}
    char_count = 0
    lowercase_string = text.lower()
    for char in lowercase_string:
        if char not in characters:
            char_count = lowercase_string.count(char)
            characters[f"{char}"] = char_count
    return characters

#Sorts Character Dictionary
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
