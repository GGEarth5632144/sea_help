#5.10
import sys
number_of_parameters = len(sys.argv) - 1
if number_of_parameters == 0:
    print("none")
else:
    check  = input("What was the parameter? ")
    if check == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")