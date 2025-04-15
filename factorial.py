# Write a Python function factorial(num) which returns the factorial of a given number.

def factorial(num):
    results = 1
    for num2 in range (1,num + 1):
        results *= num2
    return results

my_test_num = 3
print(factorial(my_test_num))