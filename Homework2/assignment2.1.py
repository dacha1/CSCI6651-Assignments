count = 0
def guess(startNo,endNo):
    global count
    count += 1
    midNo = (startNo + endNo)//2
    response = input("Is it" + str(midNo) + "? (yes/no) : ")
    if response == "Yes" or response == "yes":
        print("Yeey! I got it in" + str(count) + "tries!")
        response = input("Do you want to play more? (yes/no): ")
        if response == "Yes" or response == "yes":
            count = 0
            guess(1,100)
        else:
            print("Bye-bye")
            return False
    elif response == "No" or response == "no":
        response = input("Is the number larger than" + str(midNo) + "? (yes/no): ")
        if response == "Yes" or response == "yes":
            return guess(midNo+1, endNo)
        elif response == "No" or response == "no":
            return guess(startNo, midNo-1)
        
name = input("Hi, what is your Name? ")
print("Hello" + name + "!", "Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")
guess(1,100)
        
