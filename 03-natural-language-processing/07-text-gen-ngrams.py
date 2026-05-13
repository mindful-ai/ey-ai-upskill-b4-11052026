import random
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Example corpus (for simplicity, using a small set of sentences)
corpus = """
O gentle night, that veils the weary world in sable grace, attend my whisper’d thoughts. The moon, a pale and watchful queen, doth climb her throne amidst the trembling stars, while mortal hearts lie restless in their silent chambers. What fickle fortune governs man, that in his brightest hour there lurks the shadow of despair?
I wander thus, a pilgrim of my own unrest, seeking in the hush some counsel for the soul. The wind, soft-tongued and wandering, speaks riddles through the leaves, yet yields no answer fit for troubled minds. Is love a balm, or but a sweeter wound, that bleeds unseen beneath a smiling guise?
Methinks the world a stage of fleeting scenes, where joy and sorrow dance in equal turn. Today a crown, tomorrow but a sigh; today fair promise, then a broken vow. Yet still we strive, as though eternity were ours to claim, though time doth mock our frail ambition.
So let me stand, though storms assail my course, and bear with steadfast heart what fate bestows. For in endurance lies a quiet strength, and in the dark, the promise of the dawn.
"""

# Tokenize the text into words
tokens = word_tokenize(corpus.lower())

# Generate bigrams (2-grams)
bigrams = list(ngrams(tokens, 2))

# Create a dictionary to store bigrams
bigram_dict = {}
for w1, w2 in bigrams:
    if w1 in bigram_dict:
        bigram_dict[w1].append(w2)
    else:
        bigram_dict[w1] = [w2]

# Function to generate text
def generate_text(start_word, length=10):
    current_word = start_word
    generated_text = [current_word]
    
    for _ in range(length - 1):
        if current_word in bigram_dict:
            next_word = random.choice(bigram_dict[current_word])  # Randomly pick the next word
            generated_text.append(next_word)
            current_word = next_word  # Update the current word to the new word
        else:
            break  # If the current word doesn't have any following words, stop generation

    return ' '.join(generated_text)

# Generate text starting with 'i'
generated_text = generate_text('pilgrim', 15)
print("Generated Text:", generated_text)


'''
We started with the word "i" and generated a sequence of 10 words.
The model used the bigram dictionary to predict the next word based on the preceding word. For example:
After "i", the next word could be "love", so it picked "love".
After "love", it picked "programming", and so on.


This example uses a simple bigram model, where the text is generated word 
by word based on the immediate previous word. More complex models like trigrams 
or even higher-order N-Grams can be used for better text generation that captures 
more context.

For larger corpora or more coherent text generation, you could use more 
sophisticated models, such as Recurrent Neural Networks (RNNs) or GPT-based models. 
However, for small-scale tasks, N-grams provide a simple and effective way to 
generate text based on observed word patterns.

'''