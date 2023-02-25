import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

sentence = "I am feeling very happy today."

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Use the polarity_scores method to get a dictionary of scores for the sentence
scores = sia.polarity_scores(sentence)

# Extract the compound score (a measure of overall sentiment)
compound_score = scores["compound"]

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Define a list of keywords related to self-confidence
confidence_keywords = ["happy", "confident", "proud", "successful", "accomplished"]

# Initialize a variable to keep track of the number of confidence-related keywords found in the sentence
confidence_count = 0

# Loop through the tokens and check for confidence-related keywords
for token in tokens:
    if token in confidence_keywords:
        confidence_count += 1

# Calculate the proportion of confidence-related keywords in the sentence
confidence_proportion = confidence_count / len(tokens)

# Print the compound score and confidence proportion
print("Compound Score:", compound_score)
print("Confidence Proportion:", confidence_proportion)