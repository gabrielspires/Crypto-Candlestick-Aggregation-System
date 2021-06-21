FROM python:3.8.5

# Installs poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Creates the alias so that you dont need to use the full poetry path to run it inside the container
RUN echo "source /root/.poetry/env" >> /root/.bashrc

COPY ./candlestick_aggregator /app/candlestick_aggregator
COPY pyproject.toml python.dockerfile /app/
WORKDIR /app

# Installs python dependencies using poetry
RUN /root/.poetry/bin/poetry install