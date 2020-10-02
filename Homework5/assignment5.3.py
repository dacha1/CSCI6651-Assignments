import time
import math

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - start)
        return f
    return wrapper
@timer
def factorial(num):
    return math.factorial(num)
f = factorial(3456)

