import pickle
from sklearn.preprocessing import LabelEncoder

class Model:
    @staticmethod
    def carrega_modelo(path):
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    @staticmethod
    def preditor(model, X_input):
        return model.predict(X_input)
