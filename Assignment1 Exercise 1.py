# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is
# equal to or lower than 1000. Otherwise,return their sum.
def multiply_sum(num1,num2):
    product = num1*num2
    if product<=1000:
        return product
    else:
        sum = num1 + num2
        return sum
result = multiply_sum(20,30)
print("The result is ",result)
result = multiply_sum(40,30)
print("The result is",result)
