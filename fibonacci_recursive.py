def fibonnaci(n):
    if n < 0:
        return "Only positive integers"
    if n <= 1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

# Constraints
# n >= 0 and n <= 30

while True:
    n = int(input("Please pick a number between 0-30 "))
    print(fibonnaci(n))

