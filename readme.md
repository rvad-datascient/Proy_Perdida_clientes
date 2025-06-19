**💼 Predicción de Fuga de Clientes Bancarios con Machine Learning**

Este proyecto de Machine Learning busca predecir la probabilidad de que un cliente bancario abandone el servicio. Implementa un pipeline completo, desde la limpieza de datos hasta el modelado y análisis con SHAP para la interpretabilidad.

Además, cuenta con una aplicación interactiva en Streamlit, que permite analizar clientes individuales y visualizar los factores que influyen en su decisión.

**📂 Estructura del Proyecto**

proyecto_fuga_clientes/
├── README.md                   # 📌 Documentación del proyecto
├── 01_Data/                    # 📂 Datos originales
│   ├── Seg_Clientes.csv        # Dataset de clientes
├── 02_src/                     # 📂 Código fuente modular
│   ├── cargar_csv.py           # Carga de datos
│   ├── limpieza_datos.py       # Preprocesamiento y transformación
│   ├── winsorizer.py           # Winsorización de variables
│   ├── division_datos.py       # División en train/test
│   ├── evaluacion_modelos.py   # Métricas y validación cruzada
│   ├── seleccion_modelo.py     # Ajuste de hiperparámetros y elección del mejor modelo
│   ├── guardar_modelo.py       # Serialización con joblib
│   ├── prediccion_nuevo.py     # Predicción sobre nuevos datos
├── 03_notebooks/               # 📂 Notebooks de análisis exploratorio
│   ├── env__0_datos_+_eda_predicción_de_la_pérdida_de_clientes_bancarios.py
│   ├── env__1_limpieza_datos_y_feature_predicción_de_la_pérdida_de_clientes_bancarios.py
├── 05_ml_project/               # 📂 Modelos entrenados y aplicación
│   ├── app.py                  # Aplicación Streamlit
│   ├── modelo_fuga_clientes.pkl # Modelo entrenado
│   ├── scaler_robust_fuga_clientes.pkl  # Scaler para normalización de datos
│   ├── requirements.txt         # Dependencias necesarias

**🚀 Instalación y Uso**

**1️⃣ Clona el repositorio**
git clone https://github.com/rvad-datascient/Proy.-Impago-hipotecas.git
cd proyecto_fuga_clientes

**2️⃣ Crear un entorno virtual y activarlo**
python -m venv env
source env/Scripts/activate  # Windows

**3️⃣ Instalar las dependencias**
pip install -r requirements.txt

**4️⃣ Ejecutar la aplicación Streamlit**
streamlit run 05_ml_project/app.py

📌 La aplicación permite ingresar datos de un cliente y visualizar la probabilidad de fuga.

**5️⃣ Entrenar el modelo (opcional) Si deseas entrenar el modelo desde cero:**
python 02_src/evaluacion_modelos.py

Esto generará modelo_fuga_clientes.pkl, listo para hacer predicciones.

**🛠 Tecnologías Utilizadas**
✅ Python 3.9+ ✅ Scikit-learn, XGBoost, LightGBM - Modelos de Machine Learning ✅ SHAP - Interpretabilidad del modelo ✅ Streamlit - Aplicación interactiva ✅ Pandas & NumPy - Manipulación de datos ✅ Matplotlib & Seaborn - Visualización

**📊 Aplicaciones en el Mundo Real**
Este modelo puede aplicarse en entornos bancarios y financieros para: ✔️ Anticipar la fuga de clientes ✔️ Mejorar estrategias de retención ✔️ Optimizar asignación de recursos ✔️ Integración en CRM para personalización de campañas

**📜 Licencia**
Este proyecto está bajo Licencia MIT, lo que significa que puedes usarlo, modificarlo y compartirlo libremente citando al autor.

**💡 Sobre Mí**
👋 ¡Hola! Soy Raquel, apasionada por la Data Science y el Machine Learning. Me especializo en convertir datos en conocimiento útil, desarrollando soluciones tecnológicas que impactan y generan valor.

📊 Mis áreas de especialización incluyen: ✅ Modelado predictivo y aprendizaje automático ✅ Análisis de datos y optimización de estrategias ✅ Interpretabilidad de modelos con SHAP y técnicas avanzadas ✅ Desarrollo de aplicaciones interactivas con Streamlit
