"""
Este script contém a implementação de testes para um modelo de previsão de churn (cancelamento) de clientes utilizando o algoritmo CART. 
As principais funcionalidades incluem:

1. Carregamento e pré-processamento de dados de um arquivo CSV.
2. Carregamento de um modelo treinado e um scaler a partir de arquivos pickle.
3. Avaliação do modelo utilizando as métricas de acurácia e precisão.

Para testar o código utilize o comando pytest test_model.py

É recomendado o uso de ambiente virtual

"""

import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import accuracy_score, precision_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from classes.carregador import Carregador
from classes.model import Model
from classes.avaliador import Avaliador


def preprocessar_dados(df):
    """Preprocessa os dados de entrada, convertendo strings para valores numéricos"""
    
    # Remover a coluna 'customerID', se ela existir
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)
    
    # Definir colunas relevantes baseadas no seu modelo anterior
    relevant_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'OnlineSecurity', 'TechSupport', 'PaperlessBilling', 'DeviceProtection', 'OnlineBackup', 'PaymentMethod']
    
    df = df[relevant_features + ['Churn']]
    
    # Corrigir colunas numéricas que podem ter valores inválidos
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # Preencher valores nulos que surgiram após a conversão
    df = df.fillna(0)

    # Converter colunas categóricas para valores numéricos
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
    
    return df

# Parâmetros
url_dados = "./model/WA_Fn-UseC_-Telco-Customer-Churn.csv"
modelo_path = './model/modelo_cart_ajustado.pkl'
scaler_path = './model/scaler.pkl'  

# Teste do modelo CART
def test_modelo_cart():
    # Carregando dados
    dataset = Carregador.carregar_dados(url_dados)
    
    # Preprocessando dados
    dataset = preprocessar_dados(dataset)
    
    # Separando features e target
    X = dataset.drop('Churn', axis=1)
    y = dataset['Churn']
    
    # Dividindo em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)
    
    # Carregando scaler
    scaler = Model.carrega_modelo(scaler_path)
    
    # Aplicando scaler
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Carregando modelo
    modelo = Model.carrega_modelo(modelo_path)
    
    # Avaliando o modelo
    metricas = Avaliador.avaliar(modelo, X_test_scaled, y_test)
    
    # Testando as métricas
    assert metricas['accuracy'] >= 0.70, f"Acurácia muito baixa: {metricas['accuracy']}"
    assert metricas['precision'] >= 0.60, f"Precisão muito baixa: {metricas['precision']}"
  
    # Mensagem de alerta
    print("Modelo CART passou em todos os testes!")
    print(f"Métricas: {metricas}")

if __name__ == "__main__":
    test_modelo_cart()

