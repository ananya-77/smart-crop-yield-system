import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
crop_data = pd.read_csv('../data/Crop_recommendation.csv')
weather_data = pd.read_csv('../data/weatherHistory.csv')

# Visualizations
sns.pairplot(crop_data)
plt.savefig('crop_pairplot.png')
plt.show()

sns.heatmap(crop_data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Crop Yield Correlation')
plt.savefig('crop_heatmap.png')
plt.show()

# Visualize Weather Data
sns.lineplot(data=weather_data, x='Formatted Date', y='Temperature (C)', label='Temperature')
sns.lineplot(data=weather_data, x='Formatted Date', y='Humidity', label='Humidity')
plt.title('Weather Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.savefig('weather_trends.png')
plt.show()
