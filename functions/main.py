# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return(f'Hello, {name}!')

def add(x,y,z):
    sum = x + y + z
    return sum

def positive(number):
    positive = number > 0
    return positive

def negative(number):
    negative = number < 0
    return negative

greet('bob')
result = add(5,3,2)
print(result)
print(positive(5.5), positive(-1.3))
print(negative(5.5), negative(-1.3), negative(0))
