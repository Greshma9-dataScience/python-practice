Logical operators are used to combine multiple conditions.
Python has 3 logical operators:
-and
-or
-not

💻 Practice Program

age = 20
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

Output:

True
True
False

🌍 Real-World Example
ATM Withdrawal

balance = 5000
pin_correct = True

print(balance > 0 and pin_correct)

Output:
True