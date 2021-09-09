from helpers import get_countries

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


def shortest_names(countries):

    shortest_names_list = []
    shortest_name_lenght = len(countries[0])

    for country in countries:
        if len(country) < shortest_name_lenght:
            shortest_name_lenght = len(country)
            shortest_names_list = [country]
        elif len(country) == shortest_name_lenght:
            shortest_names_list.append(country)

    return shortest_names_list


def most_vowels(countries):

    vowels = ["a", "e", "i", "o", "u"]
    vowel_num_in_countries = []
    
    # def num_vowels(country):
    #     vowel_count = 0
    #     for letter in country:
    #         vowel_count = vowel_count + 1
    #     return vowel_count

    # vowel_num_in_countries = sorted(countries, key=num_vowels, reverse=True)
    # top_three_countries = vowel_num_in_countries[0:3]
    
    
    for country in countries:
        vowel_count = len([letter for letter in country if letter.lower() in vowels])
        vowel_num_in_countries.append((vowel_count, country))

    # for country in countries:
    #     vowel_count = 0
    #     for letter in country:
    #         vowel_count = vowel_count + 1
    #     vowel_num_in_countries.append((vowel_count, country))

    vowel_num_in_countries.sort(reverse=True)
    top_three_tupples = vowel_num_in_countries[0:3]
    top_three_countries = [tuple[1] for tuple in top_three_tupples]
   

    
    return top_three_countries


# takes a list of country names
# and returns a list of country names
# whose letters can be combined to form the complete alphabet.
def alphabet_set(countries):

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    countries_forming_alphabet = []

    for country in countries:
        country_removed_letters = False
        for letter in country:
            if letter in alphabet:
                alphabet.remove(letter)
                # check if country name has any letters which
                # weren't in previous countries names
                country_removed_letters = True
        # if country name removed additional letters from the alphabet, 
        # add it to the list
        if country_removed_letters:
            countries_forming_alphabet.append(country)
        # stop adding countries to the list if all the alphabetic letters have been deleted)
        if len(alphabet) == 0:
            break
        else:
            continue

    return countries_forming_alphabet


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

    #print(shortest_names(countries))
    print(most_vowels(countries))
    #print(alphabet_set(countries))
