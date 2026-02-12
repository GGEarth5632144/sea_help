#5.12
import sys
number_of_parameters = len(sys.argv) - 1
if number_of_parameters == 0:
    print("none")
else:
    for i in range(1, number_of_parameters + 1):
        show_z = ""
        for char in sys.argv[i]:
            if char == 'z' or char == 'Z':
                show_z += 'z'
        print(show_z)