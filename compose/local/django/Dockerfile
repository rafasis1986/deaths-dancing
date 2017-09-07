FROM rafasis1986/python-mysql:3.6

ENV PYTHONUNBUFFERED 1

COPY ./endpoint/requirements /requirements
RUN pip install --no-cache-dir -r /requirements/base.txt

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh \
    && chmod +x /start.sh

WORKDIR /app
