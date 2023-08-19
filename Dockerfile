FROM python:3.11.4-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install poetry
RUN poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
