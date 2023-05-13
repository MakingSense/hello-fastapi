FROM node:20 AS verify-format
WORKDIR /code
COPY package.json yarn.lock ./
RUN yarn
COPY . .
RUN yarn verify-format && yarn verify-spell

FROM koalaman/shellcheck-alpine:v0.9.0 as verify-sh
WORKDIR /code
COPY ./*.sh ./
RUN shellcheck -e SC1091,SC1090 ./*.sh

FROM python:3.11.3-bullseye AS restore
WORKDIR /code
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

FROM restore AS code
COPY ./app ./app

FROM code AS test
# TODO: run tests
RUN echo RUN TESTS HERE!

FROM code AS final
EXPOSE 80
ARG version=unknown
# TODO: change wwwroot for FastAPI convention
RUN mkdir -p /app/wwwroot/ && echo $version > /app/wwwroot/version.txt
LABEL name="hello-fastapi" version="$version"
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
