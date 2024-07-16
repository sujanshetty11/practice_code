# Take input as a string and then convert to integer
decimal_number = int(input("\n"))

# Convert to binary representation
binary_representation = bin(decimal_number)[2:]

# Print the binary representation
print(f"The binary representation of {decimal_number} is {binary_representation}")