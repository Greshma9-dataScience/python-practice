for i in range(1, 11):
    if i == 6:
        break
    print(i)

Output
1
2
3
4
5

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output 
1
2
4
5

mini practice 
for i in range(1, 11):
    if i == 8:
        break
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)