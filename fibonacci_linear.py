def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n): #this is looping
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(5))
print(fibonacci(8))
print(fibonacci(20))



# def fibi(n):
#     """ iterative version of the Fibonacci function """
#     old, new = 0, 1
#     if n == 0:
#         return 0
#     for i in range(n-1):
#         old, new = new, old + new
#     return new