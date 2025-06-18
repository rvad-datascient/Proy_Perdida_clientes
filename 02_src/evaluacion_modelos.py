  
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from lightgbm import LGBMClassifier

def evaluar_modelos(X_train, y_train):
    modelos = {
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
        "LightGBM": LGBMClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42, class_weight='balanced')
    }

    scoring = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    resultados = []

    for nombre, modelo in modelos.items():
        pipe = ImbPipeline(steps=[
            ('winsor', Winsorizer(columns=['Age', 'CreditScore'])),
            ('smote', SMOTE(random_state=42)),
            ('scaler', StandardScaler()),
            ('model', modelo)
        ])
        scores = cross_validate(pipe, X_train, y_train, scoring=scoring, cv=5)

        resultados.append({
            'Modelo': nombre,
            'Accuracy': np.mean(scores['test_accuracy']),
            'Precision': np.mean(scores['test_precision']),
            'Recall': np.mean(scores['test_recall']),
            'F1 Score': np.mean(scores['test_f1']),
            'ROC AUC': np.mean(scores['test_roc_auc'])
        })

    return pd.DataFrame(resultados).sort_values(by='ROC AUC', ascending=False).reset_index(drop=True)
