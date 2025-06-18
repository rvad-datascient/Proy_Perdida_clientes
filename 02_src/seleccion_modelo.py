  
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, classification_report
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from lightgbm import LGBMClassifier

def seleccionar_mejor_modelo(X_train, X_test, y_train, y_test):
    finalistas = {
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
        "LightGBM": LGBMClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42, class_weight='balanced')
    }

    for nombre, modelo in finalistas.items():
        print(f"
 Entrenando y evaluando: {nombre}")

        pipeline = ImbPipeline(steps=[
            ('winsor', Winsorizer(columns=['Age', 'CreditScore'])),
            ('smote', SMOTE(random_state=42)),
            ('scaler', StandardScaler()),
            ('model', modelo)
        ])

        pipeline.fit(X_train, y_train)
        y_probs = pipeline.predict_proba(X_test)[:, 1]
        prec, rec, thresholds = precision_recall_curve(y_test, y_probs)
        f1_scores = 2 * (prec * rec) / (prec + rec + 1e-8)
        best_threshold = thresholds[f1_scores.argmax()]
        print(f" Mejor umbral por F1-score: {best_threshold:.3f}")

        y_pred_ajustado = (y_probs >= best_threshold).astype(int)
        print("
 Informe de clasificación final:")
        print(classification_report(y_test, y_pred_ajustado))

        plt.figure(figsize=(10, 6))
        plt.plot(thresholds, prec[:-1], label='Precisión', linestyle='--')
        plt.plot(thresholds, rec[:-1], label='Recall', linestyle='-')
        plt.xlabel("Umbral de decisión")
        plt.ylabel("Valor")
        plt.title("Curva Precisión vs Recall según umbral")
        plt.legend()
        plt.grid(True)
        plt.show()
