# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, greeting=None):
    # return a string where <name> in the greeting template
    # is replaced by the name given in the first parameter

    if greeting is None:
        # If greeting is empty, set to default   
        greeting = f"Hello, {name}!"
        return greeting
    else:
        # If a greeting is given, replace '<name>' with the argument name
        greeting = greeting.replace("<name>", name)
        return greeting


def force(mass, body="earth"):
    # return the force that is exerted given the mass and body
    
    force = mass * body_gravity[body]
    return force


def pull(m1, m2, d):
    # return the gravitional pull that the two objects m1 and m2
    # which are d meters apart, have on each other

    G = 6.674 * 10 ** -11
    pull = G * ((m1 * m2) / d ** 2)
    return pull


# Where is the correct place for this dictionary?
# Inside or outsde the functions? 
# If outside, before or after function definitions?
body_gravity = {
    "sun": 274.0,
    "jupiter": 24.9,
    "neptune": 11.2,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6,
}


# testing functions
print(greet("Bob",))
print(pull(800, 1500, 3))
print(force(0.1, "sun"))
