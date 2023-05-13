import copy
import random

test_text = [random.randrange(101) for iteration in range(100)]


def text_into_binary(array_of_text: list):
    final_form = []
    for number in array_of_text:
        bin_word_container = bin(number)
        final_form.append([bin_word_container.removeprefix('0b'), number])
    return final_form


def comparison_more(key, comparable):
    if len(comparable) > len(key):
        return False
    elif len(comparable) < len(key):
        return True
    for sign in range(len(key)):
        if int(key[sign]) > int(comparable[sign]):
            return True
        elif int(key[sign]) < int(comparable[sign]):
            return False
    return True


def search_the_greatest(search_results):
    greatest = search_results[0]
    for pair in search_results:
        if not comparison_more(greatest[0], pair[0]):
            greatest = copy.deepcopy(pair)
    return greatest


def search_the_lowest(search_results):
    lowest = search_results[0]
    for pair in search_results:
        if comparison_more(lowest[0], pair[0]):
            lowest = copy.deepcopy(pair)
    return lowest


def search_near(key_word, search_location, top=False, bottom=False):
    result = []
    key_word = key_word[0]
    if bottom:
        search_preprocessed = []
        for pair in search_location:
            if comparison_more(key_word[0], pair[0]):
                search_preprocessed.append(pair)
        if len(search_preprocessed) > 0:
            nearest_bottom = search_the_greatest(search_preprocessed)
            result.append(nearest_bottom)
    if top:
        search_preprocessed = []
        for pair in search_location:
            if not comparison_more(key_word[0], pair[0]):
                search_preprocessed.append(pair)
        if len(search_preprocessed) > 0:
            nearest_top = search_the_lowest(search_preprocessed)
            result.append(nearest_top)
    return result


def max_equivalence(key, comparable):
    counter = 0
    max_sign = min(len(key[0]), len(comparable[0]))
    for sign in range(max_sign):
        if key[0][sign] == comparable[0][sign]:
            counter+=1
    return counter


def search_max_equivalent(key_word, search_location):
    list_of_counters = []
    result = []
    key_word = key_word[0]
    maximal_possible = max_equivalence(key_word, key_word)
    for pair in search_location:
        list_of_counters.append([max_equivalence(key_word, comparable=pair), pair])
    maximal = list_of_counters[0]
    for counter in list_of_counters:
        if counter[0] == maximal_possible:
            result.append(counter)
        elif counter[0] > maximal[0]:
            maximal = copy.deepcopy(counter)
    result.append(maximal)
    return result


def show_search_result_near(search_result_options):
    print('Search nearest\n')
    for search_result in search_result_options:
        print('Binary form:', search_result[1], '\nDecimal form:', search_result[0], end='\n')


def show_search_result_max_equivalent(search_result_options):
    print('Search mas equivalence\n')
    for search_result in search_result_options:
        print('Binary form:', search_result[1][0], '\nDecimal form:', search_result[1][1], '\nNumber of equal signs:',
              search_result[0], end='\n')


def main():
    search_location = text_into_binary(test_text)
    user_input = 'Yes'
    while user_input != 'exit':
        user_input = input('\nInput search key\n')
        search_key = text_into_binary([int(user_input)])
        if user_input != 'exit':
            show_search_result_near(search_near(key_word=search_key, search_location=search_location,
                                                top=True, bottom=True))
            show_search_result_max_equivalent(search_max_equivalent(key_word=search_key,
                                                                    search_location=search_location))


if __name__ == '__main__':
    main()