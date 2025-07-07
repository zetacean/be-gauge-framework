FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

USER root

# Instalación de Node.js (última versión estable), Gauge y dependencias necesarias
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    curl -SsL https://downloads.gauge.org/stable | sh

# Instala dependencias Python como root
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Cambia a vscode para instalar plugins de Gauge en su home
USER vscode
RUN gauge install python && \
    gauge install html-report && \
    gauge install xml-report && \
    gauge install flash && \
    gauge install spectacle
