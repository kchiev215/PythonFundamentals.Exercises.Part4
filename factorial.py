# n >= 0 n < 995

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
factorial loops until it gets to 1.

# def fact(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

while True:
    number = int(input("Give me a number "))
    print(factorial(number))


