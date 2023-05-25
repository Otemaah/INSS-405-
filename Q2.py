
import random

# Generate 100 random numbers
random_numbers = []
for i in range(100):
    num = random.randint(1, 10000)
    random_numbers.append(num)


def sort_numbers(numbers):
    num=numbers.sort()
    return num



print('Random Numbers (before sorting):')

print(random_numbers)

#Sort the numbers
sortedArray=sort_numbers(random_numbers)

print('\nSorted Numbers:')
print(random_numbers)

