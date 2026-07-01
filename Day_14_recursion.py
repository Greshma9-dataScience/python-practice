1️⃣ Simple Recursion
Python

def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)

countdown(5)
Output
Plain text
5
4
3
2
1
Done!

2️⃣ Factorial Using Recursion
Python

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
Output
Plain text
120

3️⃣ Sum of Natural Numbers
Python

def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))
Output
Plain text
15

🌍 Real-World Example
Python

def print_files(level):
    if level == 0:
        return

    print("Folder Level:", level)
    print_files(level - 1)

print_files(3)
Output
Plain text
Folder Level: 3
Folder Level: 2
Folder Level: 1

🧠 Key Learning


A recursive function calls itself.

Every recursive function must have a base case to stop recursion.

Without a base case, recursion continues indefinitely and results in a RecursionError.

Recursion is commonly used for tree structures, searching, and mathematical problems.

🚀 Mini Practice

Print Numbers from 1 to N
Python

def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)


Find Power of a Number
Python


def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 4))