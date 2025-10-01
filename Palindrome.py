# Palindrome Check
def is_palindrome(s):
    s = s.lower().replace(" ", "")   # ignore case and spaces
    return s == s[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print(f'"{text}" is a Palindrome.')
else:
    print(f'"{text}" is NOT a Palindrome.')
