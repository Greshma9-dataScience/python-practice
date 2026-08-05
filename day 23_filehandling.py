Concepts Covered
open()
Read Mode ("r")
Write Mode ("w")
Append Mode ("a")
Closing Files
with open()


1️⃣ Create & Write to a File
file = open("sample.txt", "w")

file.write("Hello, Python!\n")
file.write("Welcome to File Handling.")

file.close()

2️⃣ Read a File
file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()

Output
Hello, Python!
Welcome to File Handling.

3️⃣ Append Data to a File
file = open("sample.txt", "a")

file.write("\nLearning Python is fun!")

file.close()

4️⃣ Using with open()
with open("sample.txt", "r") as file:
    print(file.read())

Output
Hello, Python!
Welcome to File Handling.
Learning Python is fun!