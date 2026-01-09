import os
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(L[0][0])  # Apple
print(L[1][1])  # Python
print(L[2][2])  # Bob

print([d for d in os.listdir('.') ])