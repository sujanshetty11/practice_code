def check_vowel_or_consonant(char):
    return "Vowel" if char.lower() in 'aeiou' else "Consonant" if char.isalpha() else "Not an alphabet character"

# Take input from user
character = input("Enter a character: ")

# Call the function and print the result
result = check_vowel_or_consonant(character)
print(f"The character '{character}' is a {result}.")
