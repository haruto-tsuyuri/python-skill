ARG TAG=3.10-alpine3.15

ARG PACKAGE_PATH=/usr/local/lib/python3.10/site-packages


FROM python:$TAG AS builder

ENV POETRY_HOME=/usr/local

ARG WORKDIR=/usr/app

WORKDIR $WORKDIR

ARG DEV_MODE=1

# Install dependencies pcakages
RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    curl \
    libffi-dev \
    libressl \
    zlib-dev \
    jpeg-dev \
    postgresql-dev

# Install python packages
COPY pyproject.toml $WORKDIR/pyproject.toml
COPY scripts/common/installer.sh $WORKDIR/installer.sh
RUN pip install --upgrade pip \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && sh -c "$WORKDIR/installer.sh $DEV_MODE"



FROM python:$TAG AS main

ARG PACKAGE_PATH

# User And Group Information
ARG UID=1000
ARG GID=1000
ARG UNAME=python
ARG GNAME=python



ARG WORKDIR=/usr/app
WORKDIR $WORKDIR

RUN addgroup -g $GID -S $GNAME \
    && adduser -u $UID -S -G $UNAME $GNAME


# Copy installed packages
COPY --from=builder $PACKAGE_PATH $PACKAGE_PATH
COPY --from=builder /usr/local/bin /usr/local/bin



COPY . $WORKDIR

COPY scripts/docker_entrypoint.sh /usr/app/docker_entrypoint.sh



