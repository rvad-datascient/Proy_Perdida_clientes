# 💼 Predicción de Fuga de Clientes Bancarios con Machine Learning

Este proyecto tiene como objetivo predecir qué clientes bancarios tienen mayor probabilidad de abandonar el servicio. Se ha desarrollado un pipeline completo que incluye limpieza de datos, análisis exploratorio, entrenamiento de modelos y una aplicación interactiva con Streamlit.

## 🔍 Exploración y Preparación de Datos

El conjunto de datos contiene 10.002 registros y 14 variables. Durante el análisis exploratorio (EDA) se identificaron correlaciones relevantes, outliers y variables sin valor predictivo. Se aplicaron las siguientes transformaciones:

- Eliminación de columnas irrelevantes (`RowNumber`, `CustomerId`, `Surname`)
- Codificación de variables categóricas (`Gender`, `Geography`)
- Winsorización de variables numéricas (`Age`, `CreditScore`)
- Imputación de valores nulos y eliminación de duplicados

📓 Puedes consultar el análisis completo en los notebooks disponibles en la carpeta [`03_notebooks`](./03_notebooks), que incluyen:

- `env__0_datos_+_eda_predicción_de_la_pérdida_de_clientes_bancarios.py`
- `env__1_limpieza_datos_y_feature_predicción_de_la_pérdida_de_clientes_bancarios.py`

## 🤖 Modelado y Evaluación

Se probaron 10 modelos de clasificación utilizando validación cruzada y métricas como **F1-score**, **Recall** y **ROC AUC**. Tras ajustar los umbrales de decisión, se seleccionó **Gradient Boosting** como modelo final por su equilibrio entre precisión y sensibilidad:

- **F1-score**: 0.64  
- **Recall**: 62%  
- **Accuracy**: 86%

La interpretabilidad se logró con **SHAP**, destacando variables como `Age`, `Balance` y `NumOfProducts` como factores clave en la predicción.

## 🚀 Cómo Ejecutar la Aplicación

🔗 [Accede a la app aquí](https://proyperdidaclientes-ya7kak4ybujckdnzt56f5z.streamlit.app/)

## 📌 La aplicación permite ingresar datos de un cliente y visualizar la probabilidad de fuga.

## 📂 Estructura del Proyecto
```markdown
proyecto_fuga_clientes/
├── 03_notebooks/             # Notebooks de EDA y limpieza
├── 05_ml_project/            # Modelos entrenados y aplicación Streamlit
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación del proyecto
└── .gitignore
```
## 🛠 Tecnologías Utilizadas

- Python
- Scikit-learn, XGBoost, LightGBM
- SHAP
- Streamlit
- Pandas, NumPy
- Matplotlib, Seaborn

## 💡 Sobre Mí

👋 ¡Hola! Soy Raquel, profesional en transición hacia la Ciencia de Datos, con experiencia previa en análisis financiero y gestión de procesos. Me apasiona convertir datos en conocimiento útil y aplicar técnicas de Machine Learning para resolver problemas reales.

📊 Actualmente estoy formándome en modelado predictivo, interpretabilidad de modelos con SHAP y desarrollo de aplicaciones interactivas con Streamlit, como la que acompaña este proyecto.
