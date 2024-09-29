
# Título: API de Previsão de Churn - Backend em Flask

## Descrição: Este repositório contém a implementação do backend, que recebe novos dados de clientes e realiza predições de churn com base em um modelo de machine learning treinado.

## Funcionalidades: 
- Carregamento do modelo treinado.
- API RESTful que recebe dados via POST e retorna a predição de churn em formato JSON.
- Testes automatizados com PyTest para garantir a acurácia e precisão do modelo.

### Como executar

Será necessário garantir que todas as bibliotecas Python listadas no arquivo `requirements`.txt estejam instaladas. Após clonar o repositório, navegue até o diretório raiz por meio do terminal para executar os comandos a seguir.

**É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).**



```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```
