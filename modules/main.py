# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line
import this
import time
import math
from datetime import datetime
import sys
import greet


def wait(seconds):
    time.sleep(seconds)
    return


def my_sin(x):
    return math.sin(x)


def iso_now():
    now = datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M")


def platform():
    return sys.platform


def supergreeting_wrapper(name):
    return greet.supergreeting(name)


if __name__ == "__main__":
    print("waiting....")
    print(wait(3))
    print(my_sin(1.5))
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper("nikie"))
