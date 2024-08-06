import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os

# Crear el directorio models si no existe
models_dir = 'models'
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

# Cargar el dataset enriquecido
train_df = pd.read_csv('data/processed/train_enriched.csv')

# Definir características y etiqueta
features = ['TotalSF', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF']
X = train_df[features]
y = train_df['SalePrice']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')

# Guardar el modelo
model_path = os.path.join(models_dir, 'house_price_model.pkl')
joblib.dump(model, model_path)
