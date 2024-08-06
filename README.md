# House Prices Analysis
Proyecto Final - Python para Data Science

## Objetivos
Aplicar los conceptos aprendidos en clases para realizar el análisis de un dataset de su preferencia. Familiarizarse con el manejo de versiones a través de Git y ser capaz de limpiar el dataset, crear nuevas variables, visualizar e interpretar los resultados de manera efectiva.

## Estructura del Proyecto

- **01_Analisis_Exploratorio.ipynb**: Análisis inicial sobre los datos.
- **02_Limpieza_de_Datos.ipynb**: Limpieza en base al análisis anterior.
- **03_Creacion_de_Variables.ipynb**: Creación de nuevas variables a partir de las existentes.
- **04_Visualizacion.ipynb**: Visualizaciones que muestran los resultados del análisis.
- **05_Propuesta_Practica.ipynb**: Descripción de la propuesta práctica y su implementación.
- **scripts/train_model.py**: Script para entrenar el modelo de predicción de precios de casas.
- **scripts/evaluate_model.py**: Script para evaluar el modelo entrenado.
- **tests/test_data.py**: Pruebas unitarias para asegurar la calidad del dataset.

## Propuesta de Aplicación Práctica
Utilizando los hallazgos del análisis, proponemos desarrollar un modelo predictivo para estimar el precio de una casa basado en sus características. Este modelo puede ser utilizado por agentes inmobiliarios, compradores y vendedores para tomar decisiones informadas sobre precios de propiedades. Más detalles se encuentran en `05_Propuesta_Practica.ipynb`.

### Estrategia de Inversión Inmobiliaria
Proponemos una estrategia de inversión inmobiliaria que se enfoque en propiedades con características específicas (como espacio total y edad) para maximizar el retorno de inversión.

## Instrucciones para Ejecutar el Proyecto

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/SanMaBruno/House-Prices-Analysis.git
    cd House-Prices-Analysis
    ```

2. **Instalar las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Ejecutar el análisis de datos:**
    Abre y ejecuta los notebooks en el siguiente orden:
    - 01_Analisis_Exploratorio.ipynb
    - 02_Limpieza_de_Datos.ipynb
    - 03_Creacion_de_Variables.ipynb
    - 04_Visualizacion.ipynb
    - 05_Propuesta_Practica.ipynb

4. **Entrenar el modelo de predicción:**
    ```bash
    python scripts/train_model.py
    ```

5. **Evaluar el modelo de predicción:**
    ```bash
    python scripts/evaluate_model.py
    ```

## Notebooks y Scripts

- **01_Analisis_Exploratorio.ipynb**: Realiza un análisis exploratorio de los datos para entender su estructura y contenido.
- **02_Limpieza_de_Datos.ipynb**: Limpia los datos manejando duplicados, valores faltantes y outliers.
- **03_Creacion_de_Variables.ipynb**: Crea nuevas variables que pueden proporcionar información adicional o mejorar el análisis.
- **04_Visualizacion.ipynb**: Genera gráficos que representan adecuadamente los datos y ayudan a interpretar los resultados.
- **05_Propuesta_Practica.ipynb**: Presenta una propuesta práctica basada en los hallazgos del análisis de datos y describe cómo implementar la propuesta en un contexto real.
- **scripts/train_model.py**: Script para entrenar un modelo de regresión utilizando RandomForestRegressor.
- **scripts/evaluate_model.py**: Script para evaluar el modelo entrenado y calcular el error absoluto medio (MAE).
- **tests/test_data.py**: Contiene pruebas unitarias para asegurar la calidad del dataset.

## Contribuciones
Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y envía un pull request con tus cambios. Asegúrate de seguir las mejores prácticas de codificación y de documentar adecuadamente tus contribuciones.
