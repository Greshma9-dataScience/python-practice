create short, anonymous functions using the lambda keyword.

📚 Concepts Covered

Lambda Functions

Anonymous Functions

Single-line Functions

Using lambda with expressions


💻 Practice Code

1️⃣ Simple Lambda Function

square = lambda x: x * x

print(square(5))

Output

25


---

2️⃣ Lambda with Two Arguments

add = lambda a, b: a + b

print(add(10, 20))

Output

30


---

3️⃣ Lambda with map()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

Output

[1, 4, 9, 16, 25]

🌍 Real-World Example

employees = [
    ("Alice", 50000),
    ("Bob", 45000),
    ("Charlie", 60000)
]

employees.sort(key=lambda employee: employee[1])

print(employees)

Output

[('Bob', 45000), ('Alice', 50000), ('Charlie', 60000)]

🧠 Key Learning

lambda creates small anonymous functions.

Best for short operations that are used only once.

Commonly used with map(), filter(), and sorted().


🚀 Mini Practice

Double a Number

double = lambda x: x * 2

print(double(8))

Find Maximum of Two Numbers

maximum = lambda a, b: a if a > b else b

print(maximum(15, 20))

