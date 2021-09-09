from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number_of_facts):

    # create empty list which will contain unique facts
    koala_facts = []

    # generate random facts until number_of_facts is reached
    fact_counter = 0
    n = 0

    while n < 100:
        n += 1
        fact = random_koala_fact()
        # check for duplicate facts befor adding it to the list of facts
        if fact not in koala_facts:
            fact_counter += 1
            koala_facts.append(fact)
            if fact_counter == number_of_facts:
                break

    # return requested number of unique koala facts in a list
    return koala_facts


def num_joey_facts():

    # keep track of the number of joey facts
    joey_fact_counter = 0
    # create list of unique facts
    unique_facts = []

    # check if some particular fact has been generated 10 times
    flag_fact = random_koala_fact()
    flag_fact_counter = 0
    while flag_fact_counter < 10:

        # generate a random fact
        fact = random_koala_fact()
        # test if generated fact equals particular_fact
        if fact == flag_fact:
            flag_fact_counter += 1
        # skip fact if it already has been tested
        if fact not in unique_facts:
            # add fact to fact list to test
            unique_facts.append(fact)
            # check if fact contains the string joey'
            if "joey" in fact.lower():
                joey_fact_counter += 1

    return joey_fact_counter


def koala_weight():

    weight = 0

    while weight == 0:
        fact = random_koala_fact()
        if "kg" in fact:
            first_part = fact.split("kg")[0]
            words = first_part.split(" ")
            weight = int(words[-1])

    return weight


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":

    print(unique_koala_facts(50))
    print(num_joey_facts())
    print(koala_weight())
