def transform_string(s: str, n: int) -> str:
    if n <= 0 or n > len(s):
        return "Invalid input: n must be between 1 and the length of s"
    
    result = "".join(
        char.upper() if (i + 1) % n == 0 else char.lower()
        for i, char in enumerate(s)
    )
    
    return result

s = input("Enter the string: ")
n = int(input("Enter the integer n: "))
print(transform_string(s, n))
