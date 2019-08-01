docker build -t dropbox -f ./Dockerfile .
docker run -it -p 8080:8080 --rm --name dropbox dropbox

# Jump into an sh of a running dropbox container -- $ docker exec -it dropbox /bin/sh

# Docker image related stuff

# docker tag d7d3413f68bc lordnighton/dropbox:latest
# docker push lordnighton/dropbox
# docker pull lordnighton/dropbox
# docker login --username=lordnighton // then put the password
# docker run -it -p 8080:8080 --rm --name dropbox lordnighton/dropbox
# docker save lordnighton/dropbox:latest > dropbox.tar
# zip dropbox.zip Dockerfile dropbox.py fileUploadForm.py requirements.txt templates/*

# AWS CLI related stuff
# export PATH=/Users/lordnighton/Library/Python/3.7/bin:$PATH