#!/usr/bin/env python3
f = input("What you gotta say? : ")
if f == "STOP":
    exit()
else:
    while True:
        s = input("I got that! Anything else? : ")

        if s == "STOP":
            break