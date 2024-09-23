#  Esse teste avalia a acurácia das predições do modelo

import pytest
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Carrega o modelo salvo
@pytest.fixture(scope="module")
def model():
    with open('model/modelo_cart_ajustado.pkl', 'rb') as f: # Caminho para o arquivo do modelo
        model = pickle.load(f)
    return model

# Dados de teste
@pytest.fixture(scope="module")
def simulated_data():
    data = {
    'tenure': [1, 34, 2, 2],
    'MonthlyCharges': [29.85, 56.95, 53.85, 70.7],
    'TotalCharges': [29.85, 1889.5, 108.15, 151.65],
    'Contract': ['Month-to-month', 'One year', 'Month-to-month', 'Month-to-month'],
    'OnlineSecurity': ['No', 'Yes', 'Yes', 'No'],
    'TechSupport': ['No', 'No', 'No', 'No'],
    'PaperlessBilling': ['Yes', 'No', 'Yes', 'Yes'],
    'DeviceProtection': ['No', 'Yes', 'No', 'No'],
    'OnlineBackup': ['Yes', 'No', 'No', 'No'],
    'PaymentMethod': ['Electronic check', 'Mailed check', 'Mailed check', 'Electronic check']
    }


    entrada = pd.DataFrame(data)

    # Mapeando variáveis categóricas para códigos numéricos
    categorical_columns = ['Contract', 'OnlineSecurity', 'TechSupport', 'PaperlessBilling',
                           'DeviceProtection', 'OnlineBackup', 'PaymentMethod']

    for col in categorical_columns:
        le = LabelEncoder()
        entrada[col] = le.fit_transform(entrada[col])
    
    # Convertendo para array
    X_entrada = entrada.values.astype(float)

    # Resultados esperados 
    y_test = np.array([1, 0, 0,1]) 

    return X_entrada, y_test

# Teste de desempenho
def test_model_performance(model, simulated_data):
    X_test, y_test = simulated_data
    y_pred = model.predict(X_test)

    # Calcular a acurácia
    accuracy = accuracy_score(y_test, y_pred)

    # Definir threshold mínimo (exemplo: 70%)
    assert accuracy >= 0.70, f"Expected accuracy >= 0.70 but got {accuracy}"

    print(f"Modelo passou no teste com: Accuracy: {accuracy}")

