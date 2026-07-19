import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Questions and categories
X = data["question"]
y = data["category"]

# Convert text into numbers
vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_vector, y)

# Save vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

# Save model
with open("chatbot_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")