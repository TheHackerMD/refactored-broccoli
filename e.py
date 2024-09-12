def fizzBuzz(num):
    for x in range (0, num+1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        if x % 3 == 0:
            print("Fizz")
        if x % 5 == 0:
            print("Buzz")
        else:
            print(x)


fizzBuzz(100)
