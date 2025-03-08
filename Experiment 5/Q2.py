str = "Hello World! This is Dev Bansal."
vowels = "aeiouAEIOU"
vowel_count = 0
for char in str:
    if char in vowels:  
        vowel_count += 1  
print(f"Total number of vowels in the string: {vowel_count}")