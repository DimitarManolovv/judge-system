FROM python:3.9

WORKDIR /src

COPY src/ C:/judge

CMD ["python", "main.py", "src.main:judge"]

EXPOSE 80