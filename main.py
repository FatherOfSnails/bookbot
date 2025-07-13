from stats import get_words, get_character_count, sort_stats

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    word_count = get_words('books/frankenstein.txt')
    character_count = get_character_count('books/frankenstein.txt')
    stats = sort_stats(character_count)
    print(f"{word_count} words found in the document")
    print(stats)

main()