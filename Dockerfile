FROM python:3.7-stretch

WORKDIR /app

ENV PORT 80

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]
