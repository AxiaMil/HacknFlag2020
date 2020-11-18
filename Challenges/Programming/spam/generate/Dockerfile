
FROM python:2-alpine
RUN apk --no-cache add socat

WORKDIR /usr/src/app

COPY spam.py ./

EXPOSE 8080

CMD ["chmod", "+x", "/usr/src/app/spam.py"]
CMD ["socat", "TCP4-LISTEN:8080,fork", "EXEC:python2 /usr/src/app/spam.py"]
