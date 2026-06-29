

📚 Concepts Covered

Positional Arguments

Keyword Arguments

Default Arguments


💻 Practice Code

1️⃣ Positional Arguments

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce("Veshma", 21)

Output

Name: Veshma
Age: 21


---

2️⃣ Keyword Arguments

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce(age=21, name="Veshma")

Output

Name: Veshma
Age: 21


---

3️⃣ Default Arguments

def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Veshma")

Output

Hello, Guest
Hello, Veshma

🌍 Real-World Example

def calculate_bill(price, quantity=1):
    total = price * quantity
    print("Total Bill:", total)

calculate_bill(500)
calculate_bill(500, 3)

Output

Total Bill: 500
Total Bill: 1500

🧠 Key Learning

Positional arguments pass values based on their position.

Keyword arguments pass values using parameter names.

Default arguments provide a default value if no argument is given.


🚀 Mini Practice

Calculate Area of a Rectangle

def area(length, width=1):
    return length * width

print(area(10))
print(area(10, 5))

Display Student Details

def student(name, course="Python"):
    print(name, "-", course)

student("Veshma")
student("Rahul", "Data Analytics")

