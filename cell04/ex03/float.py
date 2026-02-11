#!/usr/bin/env python3

number = input("Give me a number: ")

try:
    value = float(number)

    if value.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("This is not a number.")
