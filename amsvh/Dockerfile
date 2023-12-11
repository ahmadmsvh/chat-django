FROM python:3.9-slim

WORKDIR /amsvh

COPY requirements.txt requirements.txt

COPY . . 

RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
