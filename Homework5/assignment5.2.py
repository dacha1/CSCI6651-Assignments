def bunny_ears(num_bunnies):
        if(num_bunnies == 0):
                return 0
        elif(num_bunnies % 2 == 1):
                return 2 + bunny_ears(num_bunnies - 1)
        else:
                return 3 + bunny_ears(num_bunnies - 1)

result = bunny_ears(3)
print(result)


