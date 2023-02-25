import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sentence = "I am feeling very happy today."

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Use the polarity_scores method to get a dictionary of scores for the sentence
scores = sia.polarity_scores(sentence)

# Print the scores
print(scores)
