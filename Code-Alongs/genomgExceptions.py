# Inget nytt typ.

try:
    input = int(input("Enter a number: "))
except:
    print("Invalid input, please try again.")
    input = int(input("Enter a number: "))
    

# try, except har även else och finally. Närbesläktat är raise Exception.

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")