def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    if q != 0:
        return p / q
    else:
        return "Error: Division by zero"

print("Hello! Welcome to my calculator")
p = int(input("Enter the first number: "))
q = int(input("Enter the second number: "))

operation = input('What do you want to do:\n a. Add\n b. Subtract\n c. Multiply\n d. Divide\n')

if operation == "a":
    print("Result:", add(p, q))
elif operation == "b":
    print("Result:", subtract(p, q))
elif operation == "c":
    print("Result:", multiply(p, q))
elif operation == "d":
    print("Result:", divide(p, q))
else:
    print("Invalid option selected.")
