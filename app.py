# app.py
from flask import Flask, request, jsonify  
from flask_cors import CORS  
import pickle  
import numpy as np  
import pandas as pd  
import os  
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score 

# Inicializando a aplicação Flask
app = Flask(__name__)
CORS(app)  # Habilitando CORS para permitir requisições de diferentes origens

# Carregando o modelo treinado
modelo_filename = 'model/modelo_cart_ajustado.pkl'  # Caminho para o arquivo do modelo

# Verificando se o arquivo do modelo existe
if os.path.exists(modelo_filename):
    with open(modelo_filename, 'rb') as f:  
        model = pickle.load(f)  
    print("Modelo carregado com sucesso!")
else:
    print("Erro: O arquivo do modelo não foi encontrado!")

# Função para transformar os dados recebidos do frontend
def transform_data(data):
    mapping = {
        'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
        'OnlineSecurity': {'No': 0, 'Yes': 1},
        'TechSupport': {'No': 0, 'Yes': 1},
        'PaperlessBilling': {'No': 0, 'Yes': 1},
        'DeviceProtection': {'No': 0, 'Yes': 1},
        'OnlineBackup': {'No': 0, 'Yes': 1},
        'PaymentMethod': {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}
    }

    # Transformando os dados recebidos em um formato numérico
    transformed_data = {
        'tenure': float(data['tenure']),  
        'MonthlyCharges': float(data['MonthlyCharges']),  
        'TotalCharges': float(data['TotalCharges']),  
        'Contract': mapping['Contract'].get(data['Contract'], -1),  
        'OnlineSecurity': mapping['OnlineSecurity'].get(data['OnlineSecurity'], -1),
        'TechSupport': mapping['TechSupport'].get(data['TechSupport'], -1),
        'PaperlessBilling': mapping['PaperlessBilling'].get(data['PaperlessBilling'], -1),
        'DeviceProtection': mapping['DeviceProtection'].get(data['DeviceProtection'], -1),
        'OnlineBackup': mapping['OnlineBackup'].get(data['OnlineBackup'], -1),
        'PaymentMethod': mapping['PaymentMethod'].get(data['PaymentMethod'], -1)
    }

    # Retornando os dados transformados como um array NumPy
    return np.array([list(transformed_data.values())])

# Endpoint para predição
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  
    print(f"Dados recebidos: {data}")  
    input_data = transform_data(data) 
    try:
        # Realizando a predição com o modelo carregado
        prediction = model.predict(input_data)
        print(f"Predição realizada: {prediction[0]}")  # Exibindo o resultado da predição
    except Exception as e:
        # Retornando erro caso ocorra uma exceção durante a predição
        return jsonify({'error': str(e)}), 500   
    # Retornando o resultado da predição em formato JSON
    result = {
        'prediction': int(prediction[0])  
    }   
    return jsonify(result)  

# Inicializando a aplicação
if __name__ == '__main__':
    app.run(debug=True) 




