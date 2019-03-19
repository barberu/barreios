FROM python:3.7-stretch

WORKDIR /app

ENV PORT 4000

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 4000

CMD ["python", "main.py"]
