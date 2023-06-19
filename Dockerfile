
FROM python:3.9

WORKDIR /judge

COPY main.py C:/judge/main.py
COPY offline_judge.py C:/judge/offline_judge

CMD ["python", "main.py", "src.main:judge"]

