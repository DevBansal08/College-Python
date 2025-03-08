string = input("Enter a string: ")
string = string.upper()
letter_counts = {}
for letter in string:
    if letter.isalpha():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
for letter in sorted(letter_counts):
    print(f"{letter_counts[letter]}{letter}")
