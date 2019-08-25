FROM sabelomaga/simple-http-server:latest

WORKDIR /opt/apps/simplehttpserver

COPY ./*.py ./

EXPOSE 8000

CMD ["python", "http_server.py"]