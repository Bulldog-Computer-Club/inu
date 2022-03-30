FROM python:3.9-slim
LABEL name="Inu Bot"
LABEL version="0.1.0"
LABEL maintainer="Bulldog Computer Club"

ENV PIP_NO_CACHE_DIR=false \
	POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y git
RUN pip install -U poetry

WORKDIR /usr/inu

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .

ENTRYPOINT ["python3"]
CMD ["bot.py"]
