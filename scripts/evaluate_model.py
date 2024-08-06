import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error

# Cargar el dataset enriquecido
train_df = pd.read_csv('data/processed/train_enriched.csv')

# Definir características y etiqueta
features = ['TotalSF', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF']
X = train_df[features]
y = train_df['SalePrice']

# Cargar el modelo entrenado
model = joblib.load('models/house_price_model.pkl')

# Hacer predicciones
predictions = model.predict(X)
mae = mean_absolute_error(y, predictions)
print(f'Mean Absolute Error on full dataset: {mae}')
