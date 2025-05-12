FROM python:3.13.3-alpine AS builder

SHELL ["/bin/sh", "-o", "pipefail", "-c"]

ENV HOLIDAYS_GID=1000 \
    HOLIDAYS_UID=1000 \
    VIRTUAL_ENV_DIR="/opt/holidays/.venv"

RUN apk update && apk upgrade && \
    addgroup -S -g ${HOLIDAYS_GID} user && \
    adduser -S -h /home/user -u ${HOLIDAYS_UID} -G user user && \
    mkdir -p /opt/holidays && \
    chown -R user:user /opt/holidays && \
    pip install --upgrade pip

USER user
WORKDIR /opt/holidays

COPY --chmod=444 --chown=user:user pyproject.toml ./
COPY --chmod=444 --chown=user:user requirements requirements
RUN python -m venv ${VIRTUAL_ENV_DIR} && \
    . ${VIRTUAL_ENV_DIR}/bin/activate && \
    pip install \
        --no-cache-dir \
        --upgrade pip && \
    pip install \
        --no-cache-dir \
        --requirement requirements/build.txt \
        --requirement requirements/dev.txt \
        --requirement requirements/docs.txt \
        --requirement requirements/runtime.txt \
        --requirement requirements/tests.txt

FROM python:3.13.3-alpine

SHELL ["/bin/sh", "-o", "pipefail", "-c"]

RUN apk update && \
    apk add git postgresql-client && \
    addgroup -S user && \
    adduser -S -h /home/user -G user user

ENV VIRTUAL_ENV_DIR="/opt/holidays/.venv"
ENV FORCE_COLOR=1 \
    PATH="${VIRTUAL_ENV_DIR}/bin:$PATH" \
    PYTHONUNBUFFERED=1

USER user
WORKDIR /opt/holidays

COPY --from=builder --chmod=555 --chown=user:user /opt/holidays /opt/holidays

WORKDIR /home/user
