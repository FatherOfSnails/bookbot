from stats import get_words, get_character_count, sort_stats
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    elif len(sys.argv) == 2:
        script_name = sys.argv[0]
        path_to_file = sys.argv[1]
        word_count = get_words(path_to_file)
        character_count = get_character_count(path_to_file)
        stats = sort_stats(character_count)

        print('============ BOOKBOT ============')
        print("Analyzing book found at ", path_to_file, "...", sep='')

        print("----------- Word Count ----------")
        print(f"Found {word_count} total words.")

        print ("--------- Character Count -------")
        for stat in stats:
            if stat["char"].isalpha():
                print(stat["char"] , ": " , stat["num"], sep='')
    
        print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()