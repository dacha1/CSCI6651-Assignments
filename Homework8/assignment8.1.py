class Animal():
    def _init_(self, animal):
        self.animal = animal

    def guess_who_am_i(self):
        print("Game of Guessing Animal in 3 Hints\n")
        print("I will give you 3 hints, guess what animal I am\n")
        for i in range (0,10):
            if (self.animal=="Elephant"):
                print("I have exceptional memory")
                inp=input("Who am I?:")
                if (inp=="elephant"):
                    print("You got it! I am  elephant\n")
                    break
                else:
                    print("Nope, try again!\n")
                print("I am the largest land-living mammal in the world\n")
                inp=input("Who am I?:")
                if (inp=="elephant"):
                    print("You got it! I am  elephant\n")
                    break
                else:
                    print("Nope, try again!\n")
                print("I Big Trunk")
                inp=input("Who am I?:")
                if (inp=="elephant"):
                    print("You got it! I am  elephant\n")
                else:
                    print("I'm out of hints! The answer is: Elephant\n")
                    break
            if (self.animal=="Tiger"):
                print("I am the biggest cat")
                inp=input("Who am I?:")
                if (inp=="tiger"):
                    print("You got it! I am  tiger\n")
                    break
                else:
                    print("Nope, try again!\n")
                print("I come in black and white or orange and black\n")
                inp=input("Who am I?:")
                if (inp=="tiger"):
                    print("You got it! I am  tiger\n")
                    break
                else:
                    print("Nope, try again!\n")
                print("I am wild Animal ")
                inp=input("Who am I?:")
                if (inp=="tiger"):
                    print("You got it! I am  tiger\n")
                else:
                    print("I'm out of hints! The answer is: Tiger\n")
                    break
            if (self.animal=="Bat"):
                print("I use echo-location")
                inp=input("Who am I?:")
                if (inp=="bat"):
                    print("You got it! I am  Bat\n")
                    break
                else:
                    print("Nope, try again!\n")
                print("I can fly")
                inp=input("Who am I?:")
                if (inp=="bat"):
                    print("You got it! I am  Bat\n")
                    break
                else:
                    print("Nope, try again!\n")
                print("I see well in dark")
                inp=input("Who am I?:")
                if (inp=="bat"):
                    print("You got it! I am  Bat\n")
                else:
                    print("I'm out of hints! The answer is: Bat")

e = Animal()
e.guess_who_am_i()
t = Animal()
t.guess_who_am_i()
b = Animal()
b.guess_who_am_i()
                    
                
                
                
                
                    
                
                
                    
                
            


                    
                
                    
                    
        
                    
                    
                    
                    
                
                
                
                
            
        
        
