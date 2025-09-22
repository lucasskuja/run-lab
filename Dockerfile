# Use uma imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt ./

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 8080

# Comando para iniciar o servidor
CMD ["python", "app.py"]
