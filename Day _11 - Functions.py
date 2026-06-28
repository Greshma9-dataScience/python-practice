Creating a Simple Function

def greet():
print("Hello, Welcome to Python!")

greet()

Hello, Welcome to Python!

Function with Parameters

def greet(name):
    print("Hello,", name)

greet("Greshma")
Hello, Greshma 

Function with Return Value

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

output 
30

ex:
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 2)
print("Total Amount:", total)

output 
Total Amount: 1000
