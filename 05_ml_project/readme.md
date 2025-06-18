💼 Predicción de Fuga de Clientes Bancarios con Machine Learning
Este proyecto de Machine Learning busca predecir la probabilidad de que un cliente bancario abandone el servicio. Implementa un pipeline completo, desde la limpieza de datos hasta el modelado y análisis con SHAP para la interpretabilidad.

Además, cuenta con una aplicación interactiva en Streamlit, que permite analizar clientes individuales y visualizar los factores que influyen en su decisión.

📂 Estructura del Proyecto
proyecto_fuga_clientes/
├── src/                         # Código fuente modular
│   ├── cargar_csv.py            # Carga de datos
│   ├── limpieza_datos.py        # Preprocesamiento y transformación
│   ├── winsorizer.py            # Winsorización de variables
│   ├── division_datos.py        # División en train/test
│   ├── evaluacion_modelos.py    # Métricas y validación cruzada
│   ├── seleccion_modelo.py      # Ajuste de hiperparámetros y elección del mejor modelo
│   ├── guardar_modelo.py        # Serialización con joblib
│   ├── prediccion_nuevo.py      # Predicción sobre nuevos datos
│   ├── interpretacion_shap.py   # Interpretación de resultados con SHAP
├── app.py                        # Aplicación Streamlit
├── requirements.txt               # Dependencias necesarias
├── modelo_fuga_clientes.pkl       # Modelo entrenado
├── scaler_robust_fuga_clientes.pkl # Scaler para normalización de datos
├── README.md                      # Documentación del proyecto

🚀 Instalación y Uso
1️⃣ Clona el repositorio
git clone https://github.com/tu_usuario/proyecto_fuga_clientes.git
cd proyecto_fuga_clientes

2️⃣ Instala las dependencias

pip install -r requirements.txt

3️⃣ Ejecuta la aplicación Streamlit

streamlit run app.py


La aplicación permite introducir datos de un cliente y visualizar su probabilidad de fuga, junto con una explicación gráfica del impacto de cada variable usando SHAP.

4️⃣ Entrena el modelo (opcional)
Si deseas entrenar el modelo desde cero:

python src/evaluacion_modelos.py


Esto generará modelo_fuga_clientes.pkl, listo para hacer predicciones.

🛠 Tecnologías Utilizadas
✅ Python 3.9+ ✅ Scikit-learn, XGBoost, LightGBM - Modelos de Machine Learning ✅ SHAP - Interpretabilidad del modelo ✅ Streamlit - Aplicación interactiva ✅ Pandas & NumPy - Manipulación de datos ✅ Matplotlib & Seaborn - Visualización

📊 Aplicaciones en el Mundo Real
Este modelo puede aplicarse en entornos bancarios y financieros para: ✔️ Anticipar la fuga de clientes ✔️ Mejorar estrategias de retención ✔️ Optimizar asignación de recursos ✔️ Integración en CRM para personalización de campañas

🤝 Contribuciones
Si te interesa mejorar el proyecto o agregar nuevas funcionalidades:

Haz un fork del repositorio

Crea una nueva rama (git checkout -b mejora-nueva)

Envía un Pull Request con tus mejoras

¡Toda contribución es bienvenida! 🚀

📜 Licencia
Este proyecto está bajo Licencia MIT, lo que significa que puedes usarlo, modificarlo y compartirlo libremente citando al autor.

💡 Sobre Mí
👋 ¡Hola! Soy [Tu Nombre], especialista en Data Science y Machine Learning. Me apasiona transformar datos en conocimiento y construir soluciones tecnológicas que aporten valor.

🔗 Conéctate conmigo en LinkedIn: linkedin.com/in/tu-usuario