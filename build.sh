docker build -t dropbox -f ./dropbox.Dockerfile .
docker run -it -p 8080:8080 --rm --name dropbox dropbox