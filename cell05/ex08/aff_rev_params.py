#5.8
import sys
number_of_parameters = len(sys.argv) - 1
if number_of_parameters == 0:
    print("none")
else:
    for i in range(number_of_parameters, 0, -1):
        print(sys.argv[i])