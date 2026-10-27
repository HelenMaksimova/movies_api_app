FROM python:3.12

WORKDIR /opt/tests

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY conftest.py .
COPY pytest.ini .
COPY settings.py .
COPY utils ./utils
COPY source ./source
COPY testdata ./testdata


ENV PYTHONPATH=/opt/tests

ENTRYPOINT ["pytest", "-sv"]
