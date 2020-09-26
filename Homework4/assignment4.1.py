#Define a function to convert temperature from Fahrenheit to Celsius using formula.
def Fahrenheit_to_Celsius(Tf):
    Tc = (5/9)*(Tf-32)
    return Tc

if __name__ == "__main__" :
    Tf = int(input("Enter the value of fahrenheit: "))
    print(Tf, "Fahrenheit is equal to: ", Fahrenheit_to_Celsius(Tf), "degree Celsius")
    
