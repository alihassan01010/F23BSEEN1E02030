# Exercise 4: Check if the first and last number of a list is the same
# Given 
# numbers_x=[10,20,30,40,10]
# numbers_y=[75,65,35,75,30]

def check_first_last_same(numbers):
    return numbers[0] == numbers[-1]
Numbers_x = [10, 20, 30, 40, 10]
Numbers_y = [75, 65, 35, 75, 30]
result_x = check_first_last_same(Numbers_x)
result_y = check_first_last_same(Numbers_y)
print("Numbers_x:", Numbers_x, "Result:", result_x)
print("Numbers_y:", Numbers_y, "Result:", result_y)
