# imagem Dockerhub
FROM python:alpine3.22

# Define o diretório de trabalho
WORKDIR /app

# Copia as dependencias e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta que o Uvicorn irá rodar
EXPOSE 8000

# inicia o servidor Uvicorn quando o container iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]