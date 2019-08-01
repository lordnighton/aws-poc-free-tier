FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV S3_BUCKET_NAME=my-bucket-lordnighton

COPY . .

CMD [ "python", "./dropbox.py" ]
EXPOSE 8080