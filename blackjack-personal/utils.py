#modules
from functools import reduce
import time

def update_total(hand):
    new_total = reduce(lambda a, b: a + b["value"], hand, 0)
    return new_total

def delayed_print(message, delay=.4):
    print(message)
    time.sleep(delay)