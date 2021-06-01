# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# OPDRACHT STRINGS
# Add your code after this line

# Players that scored during the match
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

# Timing of the match goals in minutes
goal_0 = 32
goal_1 = 54

# Which players scored when (using the '+' operator)
scorers = scorer_1 + ' ' + str(goal_0) + ', ' + scorer_2 + ' ' + str(goal_1)

# Which players scored when (using f-strings)
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'

#create variables that store a players full, first and
#last name, lenght of last name and shortened name 
#using slicing 
player = 'Hans van Breukelen'
first_name = player[:(player.find(' '))]
last_name = player[(player.find(' ') + 1):]
last_name_len = len(last_name)
name_short = player[0] + '. ' + last_name

# create a chant by multiplying the players first name by it's lenght
# add exlamation marks and strip the trailing space
number_chants = len(first_name)
chant = ((first_name + '! ') * number_chants).strip()

# check if the chant ends with a '!" and not a ' '
good_chant = (chant[-1] != ' ')

#print variables to check if above code works
print('scorers = ', scorers)
print('first_name = ', first_name)
print('last_name_len = ', last_name_len)
print('name_short = ', name_short)
print('chant = ', chant)
print('chant does not end with \' \' = ', good_chant)

