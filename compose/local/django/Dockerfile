FROM rafasis1986/python-mysql:3.6

ENV PYTHONUNBUFFERED 1

RUN addgroup -S django \
    && adduser -S -g django django

COPY ./endpoint/requirements /requirements

COPY ./compose/local/django/start.sh /start.sh

COPY ./endpoint /app

RUN pip install --no-cache-dir -r /requirements/dev.txt \
    && sed -i 's/\r//' /start.sh \
    && chmod +X /start.sh

WORKDIR /app

RUN chown -R django:django /app

USER django

WORKDIR /app
