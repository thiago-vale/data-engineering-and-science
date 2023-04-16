From ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install --no-cache fastapi==0.95.1 uvicorn==0.21.1

EXPOSE  8000

COPY ./src /app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0"]