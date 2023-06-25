# Imagem base
FROM python:3.9

# Diretório de trabalho
WORKDIR /appd
# Instalação das dependências

RUN pip install --upgrade pip && \
    pip install poetry

COPY  Dockerfile poetry.lock* pyproject.toml* /appd/

# Installs projects dependencies as a separate layer
RUN poetry install

# Define a variável de ambiente para o caminho do RabbitMQ
ENV CELERY_BROKER_URL amqp://guest:guest@rabbitmq:5672//

# Copiar os arquivos de configuração e código fonte
COPY . /appd/
# Comando para iniciar o Celery
CMD ["poetry", "run", "celery", "-A", "djangoproj", "worker", "--loglevel=info","-B"]
