FROM python:3.8.5

# Installs poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Creates the alias so that you dont need to use the full poetry path to run it inside the container
RUN echo "source /root/.poetry/env" >> /root/.bashrc

COPY ./app /var/tmp/www
WORKDIR /var/tmp/www

# Installs python dependencies using poetry (the alias only works after the container creation)
RUN /root/.poetry/bin/poetry install