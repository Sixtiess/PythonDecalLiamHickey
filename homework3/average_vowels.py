# File: average_vowels.py

# You're curious about the average number of vowels compared to consonants in a paragraph.

import re

VOWELS = "aeiouAEIOU"


# --- 1. Counting Vowels ---

def counting_vowels_and_consonants(text):
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in VOWELS:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)



# --- 2. Average Vowels ---

def average_vowels_and_consonants(paragraph):
    sentences = [s.strip() for s in re.split(r"[.!?]", paragraph) if s.strip()]

    total_vowels = 0
    total_consonants = 0
    for sentence in sentences:
        vowels, consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels
        total_consonants += consonants


    num_sentences  = len(sentences)
    avg_vowels = total_vowels / num_sentences
    avg_consonants = total_consonants / num_sentences
    return (num_sentences, avg_vowels, avg_consonants)


# Here is your paragraph to analyze. It is a quote from Richard Feynman.
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

num_sentences, avg_vowels, avg_consonants = average_vowels_and_consonants(paragraph)

print(f"The paragraph has {num_sentences} sentences.")
print(f"On average, each sentence has {avg_vowels:.2f} vowels and {avg_consonants:.2f} consonants.")
