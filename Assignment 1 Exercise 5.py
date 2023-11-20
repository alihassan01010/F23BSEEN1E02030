# Exercise 5 : Display numbers divisible by 5 from a list
# iterate the given list of numbers and print only those numbers which
# are divisible by 5.

numbers = [10, 20, 33, 46, 55]
print("Divisible by 5:")
for num in numbers:
    if num % 5 == 0:
        print(num)
