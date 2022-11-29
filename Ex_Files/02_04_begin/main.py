NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
print("The name and ages are: ")
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

print("\n The names are: ")

for name in NAMES:
    print(name)

print("\n Again, the name ages are: ")

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

print("\n here are the reversed name: ")

for name in reversed(NAMES):
    print(name)

print("\n Here are the ranges of the liste: ")

for i in range(5):
    print(i)

# enumerate

print("\n Here are the enumerated value of the list: ")
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
