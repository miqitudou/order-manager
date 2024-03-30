FROM python:3.10


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8090

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]
