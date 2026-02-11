#5.3
numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_numbers = []
print("Original:", numbers)
for i in range(len(numbers)):
        numbers[i] += 2
        if numbers[i] > 5:
            new_numbers.append(numbers[i])
print("New array:", set(new_numbers))