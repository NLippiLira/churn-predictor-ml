# Imagen base
FROM python:3.10-slim

# Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar proyecto completo
COPY . .

# Exponer puerto
EXPOSE 5000

# Ejecutar API
CMD ["python", "-m", "src.api.app"]