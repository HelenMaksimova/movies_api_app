FROM python:3.12

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY main.py .
COPY src ./src

ENV PYTHONPATH=/opt/app

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]