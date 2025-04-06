# Usar imagem oficial do Python
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pela API Flask
EXPOSE 5000

# Rodar o servidor
CMD ["python", "app.py"]
