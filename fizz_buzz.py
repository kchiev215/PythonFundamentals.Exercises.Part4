for number in range(1,101):
    if number == 3:
        print("Fizz")
    elif number == 5:
        print("Buzz")
    elif number%3 == 0 or number%5 ==0:
        print("FizzBuzz")
    else:
        print(f"{number} new line")
