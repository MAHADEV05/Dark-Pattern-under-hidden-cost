from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib 
from sklearn.pipeline import make_pipeline # for model persistence


texts = [
    "PRE BOOK NOW","ADD 2 ITEMS",
    "JUST ","ADD 3 ITEMS",
    "OFFER",
    "SPECIAL PRICE5",
    "BANK OFFERS ",
    "ADD ONS",
    "TOTAL",
    "11% OFF","10% OFF","20% OFF","30% OFF","40% OFF","50% OFF",
    "ADD 3 ITEMS",
]

labels = [1, 1, 1, 1, 0, 1, 0]  # 0: No hidden costs, 1: Hidden costs present

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

joblib.dump(model, "hidden_costs_model.pkl")
