def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(f"The following is a list of the characters in the text and how many of them there are: {char_count}")

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

main()