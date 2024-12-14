def main():
    book_path = "books/frankenstein.txt"
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
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

#Gets Raw Text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Counts Words In Book
def get_num_words(text):
    words = text.split()
    return len(words)

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