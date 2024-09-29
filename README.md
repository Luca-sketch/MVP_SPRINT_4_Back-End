
# Título: API de Previsão de Churn - Backend em Flask

## Descrição: 
Este repositório contém a implementação do backend, que recebe novos dados de clientes e realiza predições de churn com base em um modelo de machine learning treinado.

## Funcionalidades: 
- Carregamento do modelo treinado.
- API RESTful que recebe dados via POST e retorna a predição de churn em formato JSON.
- Testes automatizados com PyTest para garantir a acurácia e precisão do modelo.

## Rotas da API
/predict [POST]: Recebe dados de clientes em JSON e retorna a predição.

## Estrutura do Projeto

O projeto está dividido em três repositórios e um vídeo explicativo:

- [MVP_SPRINT_4_Treinamento](https://github.com/Luca-sketch/MVP_SPRINT_4_Treinamento.git): Contém o notebook de machine learning com a modelagem, otimização e treinamento do modelo preditivo. 
- [MVP_SPRINT_4_Back-end](https://github.com/Luca-sketch/MVP_SPRINT_4_Back-End.git): Implementa a API em Flask que carrega o modelo treinado e realiza as predições de churn.
- [MVP_SPRINT_4_FRONT_END](https://github.com/Luca-sketch/MVP_SPRINT_4_Front-End.git): Interface frontend para inserir novos dados e exibir as predições geradas pelo backend.
- [Vídeo](https://drive.google.com/file/d/1HQgQcQTmpStFg4wwNPHoap9S59pVbp0I/view?usp=drive_link): Vídeo com a explicação do projeto.

### Como executar

Será necessário garantir que todas as bibliotecas Python listadas no arquivo `requirements`.txt estejam instaladas. Após clonar o repositório, navegue até o diretório raiz por meio do terminal para executar os comandos a seguir.

**É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).**



```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ python app.py
```
Para executar os testes:

```
(env)$ python test_model.py
```

