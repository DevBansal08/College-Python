palindrome_list = []
armstrong_list = []
for num in range(1001):
    if str(num) == str(num)[::-1]:
        palindrome_list.append(num)
    digits = [int(d) for d in str(num)]
    power = len(digits)
    armstrong_sum = sum(d ** power for d in digits)
    if armstrong_sum == num:
        armstrong_list.append(num)
palindrome_tuple = tuple(palindrome_list)
armstrong_tuple = tuple(armstrong_list)

palindrome_set = set(palindrome_list)
armstrong_set = set(armstrong_list)
print("Palindrome Numbers (List):", palindrome_list)
print("Armstrong Numbers (List):", armstrong_list)

print("\nPalindrome Numbers (Tuple):", palindrome_tuple)
print("Armstrong Numbers (Tuple):", armstrong_tuple)

print("\nPalindrome Numbers (Set):", palindrome_set)
print("Armstrong Numbers (Set):", armstrong_set)
