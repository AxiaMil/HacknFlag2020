
FROM python:2-alpine
RUN apk --no-cache add socat

WORKDIR /usr/src/app

COPY generate.py ./

EXPOSE 8080

CMD ["chmod", "+x", "/usr/src/app/generate.py"]
CMD ["socat", "TCP4-LISTEN:8081,fork", "EXEC:python2 /usr/src/app/generate.py"]
