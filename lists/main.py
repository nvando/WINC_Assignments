# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'


# Add your code after this line
def alphabetical_order(film_names):
    sorted_list = sorted(film_names)
    return sorted_list


def won_golden_globe(film):
    winners = [x.lower() for x in ['Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']]
    if film.lower() in winners:
        return True
    else:
        return False


#def remove_toto_albums(mixed_list):
    toto_albums = [
        'Fahrenheit',
        'The Seventh One',
        'Toto XX',
        'Falling in Between',
        '35th Anniversary – Live in Poland',
        'Toto XIV',
        'Old Is New',
        'Tours Around the Sun - Live in Holland'
        ]
    for x in toto_albums:
        if x in mixed_list:
            mixed_list.remove(x)
    return mixed_list

def remove_toto_albums(mixed_list):
    if 'Fahrenheit' in mixed_list:
        mixed_list.remove('Fahrenheit')
    if 'The Seventh One' in mixed_list:
        mixed_list.remove('The Seventh One')
    if 'Toto XX' in mixed_list:
        mixed_list.remove('Toto XX')
    if 'Falling in Between' in mixed_list:
        mixed_list.remove('Falling in Between')
    if '35th Anniversary – Live in Poland' in mixed_list:
        mixed_list.remove('35th Anniversary – Live in Poland')
    if 'Toto XIV' in mixed_list:
        mixed_list.remove('Toto XIV')
    if 'Old Is New' in mixed_list:
        mixed_list.remove('Old Is New')
    if 'Tours Around the Sun - Live in Holland' in mixed_list:
        mixed_list.remove('Tours Around the Sun - Live in Holland')
    return mixed_list

    

print(remove_toto_albums([
    'The Poseidon Adventure',
    'Jaws', 'War Horse',
    'Old Is New',
    'Memoires of a Geisha',
    'Fahrenheit',
    'Superman'
    ]))
