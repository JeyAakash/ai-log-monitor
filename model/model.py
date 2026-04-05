from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

logs = [
    "User logged in",
    "File uploaded",
    "Database connection failed",
    "High memory usage",
    "Timeout occurred"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(logs)

model = IsolationForest(contamination=0.2)
model.fit(X)

def predict_log(log):
    vec = vectorizer.transform([log])
    pred = model.predict(vec)
    return "Anomaly" if pred[0] == -1 else "Normal"