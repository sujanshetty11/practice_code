import nltk 
from nltk.corpus import wordnet

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

    return antonyms,synonyms

words=input("enter the word : ")
antonym,synonym = get_a_S(words)
print(f"synonyms of the ' {words} 'is {synonym}")
print(f"antonyms of the '{words}' is {antonym}")