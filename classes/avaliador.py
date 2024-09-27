from sklearn.metrics import accuracy_score, precision_score
from classes.model import Model

class Avaliador:
    @staticmethod
    def avaliar(model, X_test, Y_test):
        predicoes = Model.preditor(model, X_test)
        return {
            'accuracy': accuracy_score(Y_test, predicoes),
            'precision': precision_score(Y_test, predicoes, average='binary'),
        }
