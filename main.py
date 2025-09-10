
import sys
from stats import dict_to_arr, get_char_dict, get_num_words


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.Exit(1)

    bookpath = sys.argv[1]
    contents = get_book_text(bookpath) 
    word_count = get_num_words(contents)
    dict = get_char_dict(contents)
    arr = dict_to_arr(dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookpath}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for x in arr:
        print(f'{x['char']}: {x['count']}')
    print('============= END ===============')




main()