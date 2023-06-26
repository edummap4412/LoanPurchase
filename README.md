# APIWORDS  
O projeto consiste em um sistema de cadastro de clientes, 
no qual os usuários fornecem informações pessoais para a análise e possível aprovação de solicitações de empréstimo. O sistema permite que os clientes registrem seus dados, os quais serão avaliados com base em critérios estabelecidos, a fim de determinar a elegibilidade para obter um empréstimo.

### Executando o Projeto com Docker
  * Certifique-se de ter o Docker instalado na sua máquina.
  * Crie uma imagem Docker a partir do Dockerfile incluído no projeto:
  
  * Execute o projeto usando o Docker Compose para inciar o Celery para fins de testes da fila:
  ```shell
    $ docker-compose up
  ```
  * Para iniciar o servidor local do app ```python manage.py runserver```
  
    Observação: Foi configurada uma fila para a execução de uma rotina que processará os dados dos clientes e suas respectivas propostas. Essa rotina realizará uma análise dos dados com base em critérios predefinidos, determinando se a proposta de empréstimo será aprovada ou não. O uso de uma fila permite que o processamento ocorra de forma assíncrona e agendada, garantindo a eficiência e escalabilidade do sistema.
---

# Endpoints

## URLS para test no Innsominia, Postman e etc..


### `/register-cli`
### Requisição
Observação: Para realizar o cadastramento do CPF, utilize o serviço disponível em https://www.4devs.com.br/gerador_de_cpf. Essa é a única validação que pode acarretar problemas de criação, portanto, é importante utilizar um CPF válido gerado por esse serviço para evitar possíveis inconsistências no cadastro.
- Método: POST
- URL: `/register-cli`
- Corpo da Requisição (JSON):
```json
  {
  "client": {
    "name": "John Doe",
    "tax_id":"632.075.000-64",
    "loan_value": "3000"
  },
  "address": {
    "street": "123 Main St",
    "state": "California",
    "number": "444"
  }
}
	
```
### Resposta

A resposta é um objeto JSON contendo a contagem de vogais para cada palavra enviada.

Exemplo de resposta bem-sucedida:
```json
{
  "message": "Usuário cadastrado com sucesso, sua solicitação de crédito está sendo avaliada"
}
```
