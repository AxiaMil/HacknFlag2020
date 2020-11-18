#!/bin/sh

PORT=${PORT:-"5000"}
docker rm -f inject-running
docker run -d -p ${PORT}:${PORT} -e PORT=${PORT} --name inject-running inject
