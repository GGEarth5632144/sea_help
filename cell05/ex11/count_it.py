#5.11
import sys
number_of_parameters = len(sys.argv) - 1
print("parameters: " + str(number_of_parameters))
if number_of_parameters == 0:
    print("none")
else:
    for i in range(1, number_of_parameters + 1):
        
        print(sys.argv[i] + ": " + str(len(sys.argv[i])))