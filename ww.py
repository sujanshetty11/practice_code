import nltk
from nltk.corpus import wordnet

# Download the 'wordnet' corpus
nltk.download('wordnet')

def get_a_S(word):
    synonyms = set()
    antonyms = set()

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    antonyms.add(ant.name())

    return antonyms, synonyms

# Get input from the user
words = input("Enter the word: ")

# Get antonyms and synonyms
antonym, synonym = get_a_S(words)

# Print the results
print(f"Synonyms of the word '{words}' are: {synonym}")
print(f"Antonyms of the word '{words}' are: {antonym}")
