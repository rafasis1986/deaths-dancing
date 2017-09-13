FROM node:8.4-slim

RUN mkdir /webapp

COPY ./compose/local/vue/entrypoint.sh /entrypoint.sh

RUN groupadd -r webapps \
    && useradd -r -g webapps web \
    && chown -R web /webapp \
    && chmod +x /entrypoint.sh \
    && chown web /entrypoint.sh

WORKDIR /webapp

ENTRYPOINT ["/entrypoint.sh"]
