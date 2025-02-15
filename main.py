def main():
    print('--- Begin report of books/frankenstein.txt ---')
    
    count = get_number_of_words()
    print(f'{count} words found in the document')
    print()
    
    char_list = get_number_of_words_ext()
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print('--- End report ---')


def get_number_of_words():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read().split()
        count = len(file_contents)
        return count


def sort_on(dict):
    return dict["num"]


def get_number_of_words_ext():
    dictionary = {}
    char_list = []
    
    with open('books/frankenstein.txt') as f:
        book = f.read()
        chars = list(book.lower())
        
        for char in chars:
            if char.isalpha():
                if char in dictionary.keys():
                    dictionary[char] += 1
                else:
                    dictionary[char] = 1
        
        for char in dictionary:
            char_dict = {"char": char, "num": dictionary[char]}
            char_list.append(char_dict)
        
        char_list.sort(reverse=True, key=sort_on)
        return char_list


main()