from flask import Flask, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model for predictions
model = joblib.load('../data/crop_yield_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend/<int:N>/<int:P>/<int:K>/<float:temperature>/<float:humidity>/<float:ph>/<int:rainfall>')
def recommend(N, P, K, temperature, humidity, ph, rainfall):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                               columns=['N', 'P', 'K', 'Temperature', 'Humidity', 'Ph', 'Rainfall'])
    recommended_crop = model.predict(input_data)[0]
    return f"Recommended Crop: {recommended_crop}"

if __name__ == '__main__':
    app.run(debug=True)
