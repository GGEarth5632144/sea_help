#5.13
import sys
number_of_parameters = len(sys.argv) - 1
if number_of_parameters == 0:
    print("none")
else:
    for i in range(1, number_of_parameters + 1):
        check = sys.argv[i]
        
        if "ism" in check.lower():
            continue
        else :
            sys.argv[i] += "ism"
            print(sys.argv[i])