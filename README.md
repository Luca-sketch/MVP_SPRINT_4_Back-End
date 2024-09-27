#Back-end (Churn Prediction API)
Definição e Propósito
Este projeto é uma API desenvolvida para prever a probabilidade de cancelamento de clientes (churn) em um serviço. A API visa substituir processos manuais e registros em papel, fornecendo um sistema eficiente para análise de dados e tomada de decisões baseadas em informações preditivas.

##Funcionamento Interno
A API foi construída utilizando o Flask como framework principal. Todas as rotas e funcionalidades podem ser testadas através da biblioteca Swagger, permitindo uma fácil interação e verificação das operações disponíveis.

##Banco de Dados
O sistema utiliza um modelo de predição carregado de um arquivo .pkl, juntamente com um scaler para normalização dos dados de entrada. A predição é realizada com base nos dados enviados via requisições POST para o endpoint /predict.

##Estrutura de Dados
Os dados de entrada esperados pela API incluem:

tenure (float): Duração do serviço em meses.
MonthlyCharges (float): Custo mensal do serviço.
TotalCharges (float): Custo total acumulado pelo cliente.
Contract (int): Tipo de contrato (0: Mês a mês, 1: Um ano, 2: Dois anos).
OnlineSecurity (int): Se o cliente possui segurança online (0: Não, 1: Sim).
TechSupport (int): Se o cliente possui suporte técnico (0: Não, 1: Sim).
PaperlessBilling (int): Se o cliente opta por cobrança sem papel (0: Não, 1: Sim).
DeviceProtection (int): Se o cliente possui proteção de dispositivo (0: Não, 1: Sim).
OnlineBackup (int): Se o cliente possui backup online (0: Não, 1: Sim).
PaymentMethod (int): Método de pagamento (0: Cheque eletrônico, 1: Cheque enviado, 2: Transferência bancária, 3: Cartão de crédito).


##Rotas
O sistema é composto por um endpoint:

/predict: Recebe dados em formato JSON e retorna a predição de churn.
Como Executar
Certifique-se de que todas as bibliotecas Python listadas no arquivo requirements.txt estejam instaladas. Após clonar o repositório, navegue até o diretório raiz através do terminal e execute os seguintes comandos:

##É fortemente recomendado o uso de ambientes virtuais, como virtualenv.

bash
Copiar código
(env)$ pip install -r requirements.txt
Este comando instala as dependências descritas no arquivo requirements.txt.

##Para executar a API, basta rodar:

bash
Copiar código
(env)$ flask run --host 0.0.0.0 --port 5000
Em modo de desenvolvimento, é aconselhável usar o parâmetro --reload, que reiniciará o servidor automaticamente após alterações no código:

bash
Copiar código
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
Abra http://localhost:5000/ no navegador para verificar o status da API em execução.

Pontos de Atenção
Para a utilização completa do sistema, é necessário uma aplicação front-end que faça requisições ao endpoint /predict da API.
