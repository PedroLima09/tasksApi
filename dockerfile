# Escolher a imagem base do Python
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos de dependências e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto dos arquivos do projeto
COPY . .

# Definir a porta que será exposta pelo container
EXPOSE 8000

# Definir o comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]