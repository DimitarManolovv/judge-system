FROM python:3.9

WORKDIR judge-system-main

COPY /src/main.py ./
COPY /src/offline_judge.py ./
COPY /src/testing1.py ./
COPY /src/testing.py ./
COPY /src/web.py ./
COPY /src/submission.py ./

CMD ["python", "main.py", "src.main:judge"]

EXPOSE 80
