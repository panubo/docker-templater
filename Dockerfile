FROM alpine:latest

MAINTAINER Andrew Cutler <andrew@panubo.com>

RUN cd / && \
  apk --update add bash curl git python && \
  curl --silent https://raw.githubusercontent.com/adlibre/python-bootstrap/master/bootstrap.sh | bash -s venv git+https://github.com/panubo/docker-templater.git#egg=templater && \
  apk del bash curl git && \
  rm -rf /var/cache/apk/*

ENTRYPOINT ["/venv/bin/templater.py"]
