NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = ''.join(NAMES[:2])
GEORGE_RINGO = ''.join(NAMES[2:])
REVERSE = ''.join(NAMES[::-1])
EVERY_OTHER = ''.join(NAMES[::2])

print("Here is the sum of the ages " + str(sum(AGES)))
print("Here is the youngest value of ages " + str(min(AGES)))
print("Here is the maximum value of ages " + str(max(AGES)))

print("His name is " + JOHN_PAUL)
print("The other guy is named " + GEORGE_RINGO)
print("Here is the reverse of names " + REVERSE)
