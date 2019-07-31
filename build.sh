docker build -t dropbox -f ./dropbox.Dockerfile .
docker run -it -p 8080:8080 --rm --name dropbox dropbox

# Jump into an sh of a running dropbox container -- $ docker exec -it dropbox /bin/sh