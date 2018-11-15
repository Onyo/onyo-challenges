FROM python:3.7.1-alpine

# FIXME: never use root in production

WORKDIR /app
ARG requirement=requirements.txt
COPY requirement*.txt ./

RUN set -x \
        && apk add -U --no-cache --virtual .build-deps \
                postgresql-dev \
                gcc \
                musl-dev \
                findutils \
        \
        && pip install -r ${requirement} \
        \
        && runDeps="$( \
                find /usr/local -type f -executable -not \( -name '*tkinter*' \) -exec scanelf --needed --nobanner --format '%n#p' '{}' ';' \
                | tr ',' '\n' \
                | sort -u \
                | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
        )" \
        && apk add --virtual .erp-rundeps $runDeps \
        && apk del .build-deps

COPY . .
