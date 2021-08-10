import random

lettersAndOtherThings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", "B", "C", "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', "W", 'X', 'Y', 'Z']
numbers = ["1", "2", "3", "4", "5", "6", "8", "8", "9", "0"]
symbols = ["!", "@", "#", "$"]

char1 = random.choice(lettersAndOtherThings)
char2 = random.choice(lettersAndOtherThings)
char3 = random.choice(lettersAndOtherThings)
char4 = random.choice(lettersAndOtherThings)
char5 = random.choice(numbers)
char6 = random.choice(lettersAndOtherThings)
char7 = random.choice(lettersAndOtherThings)
char8 = random.choice(lettersAndOtherThings)
char9 = random.choice(lettersAndOtherThings)
char10 = random.choice(numbers)
char11 = random.choice(numbers)
char12 = random.choice(numbers)
char13 = random.choice(symbols)
char14 = random.choice(symbols)

chosenPassword = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 + char11 + char12 + char13 + char14
print(chosenPassword)
