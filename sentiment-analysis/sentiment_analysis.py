from textblob import TextBlob
import csv

# Sample text data
texts = [
    "How are you ?"
]

# Analyze sentiment
results = []
for text in texts:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    results.append([text, polarity, sentiment])

# Save to CSV
with open('sentiment_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Text", "Polarity", "Sentiment"])
    writer.writerows(results)

