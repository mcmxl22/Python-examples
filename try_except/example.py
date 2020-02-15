number = input("Enter a number. ")

try:
    n = float(number)
    print(f"{n} is now a float.")
except ValueError:
    Print("Please enter a number. ")
