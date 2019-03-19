FROM python:3.7-stretch

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

# Run main.py when the container launches
CMD ["python", "barreios/main.py"]
