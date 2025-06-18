  
import joblib
import pandas as pd

def predecir_cliente(X_test, modelo_path="modelo_fuga_clientes.pkl", scaler_path="scaler_robust_fuga_clientes.pkl", umbral=0.475):
    """Carga el modelo y escalador guardados, luego predice si un nuevo cliente está en riesgo de fuga."""
    modelo = joblib.load(modelo_path)
    scaler = joblib.load(scaler_path)

    nuevo_cliente = X_test.iloc[[0]]  # Simulación de un nuevo cliente
    nuevo_cliente_escalado = scaler.transform(nuevo_cliente)

    prob_fuga = modelo.predict_proba(nuevo_cliente_escalado)[:, 1][0]
    resultado = "⚠️ Cliente con riesgo de fuga." if prob_fuga >= umbral else "✅ Cliente sin riesgo de fuga."

    return prob_fuga, resultado
