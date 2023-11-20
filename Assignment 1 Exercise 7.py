# Exercise 7 : Check Palindrome Number
def is_palindrome(number):
    str_number = str(number)
    reversed_str = str_number[::-1]
    if str_number == reversed_str:
        return True
    else:
        return False

# Example usage:
original_number = 121
if is_palindrome(original_number):
    print(f"Original number {original_number} - Yes, given number is  palindrome number.")
else:
    print(f"Original number {original_number} - No, given number is not palindrome number.")

original_number = 125
if is_palindrome(original_number):
    print(f"Original number {original_number} - Yes, given number is  palindrome number.")
else:
    print(f"Original number {original_number} - No, given number is not  palindrome number.")


