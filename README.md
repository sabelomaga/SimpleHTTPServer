# SimpleHTTPServer
A simple HTTP server implementation.

### Requirements ###

- Docker version 19.03.1 or higner
- Python version 3.6 or higher

### Instructions ###

You can run the HTTP server locally (on your computer) or on a Docker container. Please see blow examples:

- $ python http_server.py (To run it locally)
- $ docker-compose up (To run it on a Docker container)

### Testing ###

To test if the HTTP server is up and running, go to http://localhost:8000 on your browser and take a look at the response.

Note: The server listens for requests on port 8000 and not port 80.