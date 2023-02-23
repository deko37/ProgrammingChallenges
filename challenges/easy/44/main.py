#!/usr/bin/python
# Programming challeng number 18 : Fizzbuzz
import sys

if __name__ == "__main__":
    limit = 100
    if len(sys.argv) > 1:
        try:
            limit = int(sys.argv[1])
        except:
            print("The given argument is not valid")
    for i in range(1, limit + 1):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
