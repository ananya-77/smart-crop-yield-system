import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load datasets
crop_data = pd.read_csv('../data/Crop_recommendation.csv')

# Prepare data
X = crop_data[['N', 'P', 'K', 'Temperature', 'Humidity', 'Ph', 'Rainfall']]
y = crop_data['Crop']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, '../data/crop_yield_model.pkl')
