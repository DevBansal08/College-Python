# Problem: Read a file and handle FileNotFoundError.

try:
    with open("file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")