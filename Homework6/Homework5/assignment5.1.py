def my_range(start, end):
    x = start
    while x < end:
        yield x
        x = x + 2

for i in my_range(0,5):
    print(i)
