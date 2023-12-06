FROM python:3.11
WORKDIR /usr/src/striper
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./script.sh .
RUN chmod +x ./script.sh
RUN pip install -r requirements.txt
COPY . .