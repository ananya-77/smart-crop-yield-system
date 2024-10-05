import joblib
import pandas as pd

# Load the model
model = joblib.load('../data/crop_yield_model.pkl')

# Function to recommend crops
def recommend_crops(N, P, K, temperature, humidity, ph, rainfall):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                               columns=['N', 'P', 'K', 'Temperature', 'Humidity', 'Ph', 'Rainfall'])
    
    predicted = model.predict(input_data)
    return predicted[0]

# Example usage
print(recommend_crops(100, 30, 20, 25, 60, 6.5, 200))
