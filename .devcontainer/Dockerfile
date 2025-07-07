FROM mcr.microsoft.com/vscode/devcontainers/python:3.12-bullseye

USER root
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm && \
    apt-get clean

USER vscode
ENV HOME=/home/vscode
ENV PATH="${HOME}/.gauge/bin:${PATH}"

RUN curl -SsL https://downloads.gauge.org/stable | sh && \
    gauge install python && \
    gauge install html-report && \
    gauge install xml-report && \
    gauge install flash

USER root
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER vscode
