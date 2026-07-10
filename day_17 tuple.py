#creating a tuple
fruits =("Apple","Banana","Mango")
print(fruits)

#output
('Apple','Banana','Mango')

#Accessing Tuple Elements

fruits=("Apple","Banana","Mango")
print(fruits[0])
print(fruits[1])

#Tuple packing and unpacking

student=("Greshma",21,"python")
name,age,course =student

print(name)
print(age)
print(course)

#output
Greshma
21
python

#tuple methods

numbers = (10,20,30,20,40)
print(numbers.count(20))
print(numbers.count(30))

#output
2
2

#real word example
student=("Greshma","Data analyst","India")

print("Name:",student[0])
print("Role:",student[1])

#output
Name: Greshma
Role: Data analyst
Country: India
print("Country:",student[2])

#find tuple length
colors =("Red","Blus","Green")
print(len(colors))

#output
3

#iterate Through a tuple

languages = ("Python","Java","SQL")
for language in languages:
  print(language)

#OUTPUT
Python
Java
SQL
