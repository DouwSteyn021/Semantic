import spacy

# Load the 'en_core_web_md' model
nlp = spacy.load('en_core_web_md')

# Compare the similarity between three words: cat, monkey, and banana
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))  # Compute similarity between cat and monkey
print(word3.similarity(word2))  # Compute similarity between banana and monkey
print(word3.similarity(word1))  # Compute similarity between banana and cat

# Compare the similarity between tokens: cat, apple, monkey, and banana
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))  # Compute similarity between each pair of tokens

# Compare the similarity between a sentence and multiple sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)  # Compute similarity between each sentence and the model sentence
    print(sentence + " - ", similarity)

# Compare the similarity between two words: coffee and morning
word1 = nlp("coffee")
word2 = nlp("morning")
similarity = word1.similarity(word2)  # Compute similarity between coffee and morning
print(similarity)
