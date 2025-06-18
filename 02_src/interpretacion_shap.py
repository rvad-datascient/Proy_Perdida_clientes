  
import shap
import joblib
import pandas as pd

def interpretar_modelo(X_test, modelo_path="modelo_fuga_clientes.pkl", scaler_path="scaler_robust_fuga_clientes.pkl"):
    """Carga el modelo y el escalador, transforma los datos, y genera visualizaciones SHAP."""
    modelo = joblib.load(modelo_path)
    scaler = joblib.load(scaler_path)

    X_test_scaled = scaler.transform(X_test)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

    explainer = shap.Explainer(modelo, X_test_scaled)
    shap_values = explainer(X_test_scaled)

    shap.summary_plot(shap_values, X_test_scaled)  # Visualización global
    shap.plots.beeswarm(shap_values)  # Impacto individual de cada característica
