FROM python:3.12.1-alpine 
ENV PYTHONUNBUFFERED True

# install headers file
RUN apk add gcc g++ linux-headers
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

ENV APP_HOME /root
WORKDIR $APP_HOME
COPY /app $APP_HOME/app

CMD [ "python", "app/main.py"]
