FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./src ./src

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x entrypoint.sh \
  && mkdir -p /app/media /app/static \
  && chmod +x /app/media/ /app/static/

ENTRYPOINT ["/app/entrypoint.sh"]