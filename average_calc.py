# Average Calculator
# Generates 10 random numbers and calculates their average using a loop

import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100

# List to store numbers
numbers = []

# Generate random numbers
for i in range(MAX_ARRAY_SIZE):
    rand_num = random.randint(MIN_NUM, MAX_NUM)
    numbers.append(rand_num)

# Print the numbers
print("Generated numbers:")
for num in numbers:
    print(num, end=" ")
print()

# Calculate the average using a loop
total = 0
for num in numbers:
    total += num

average = total / MAX_ARRAY_SIZE

# Display the average
print("Average:", average)
