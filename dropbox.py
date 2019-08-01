from flask import Flask, request, render_template
import os
from os import path, getcwd
from os.path import join
import boto3
import time
from fileUploadForm import FileUploadForm
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['fileUploadField']
      file_name = secure_filename(f.filename)
      file_path = os.path.join(os.getcwd(), file_name)
      print ("File name = " + file_name + ", file path = " + file_path)
      f.save(file_path)

      if file_name == '':
            flash('No selected file')
            return redirect(request.url)
            
      if f and allowed_file(file_name):
         # for LOCAL development
         # session = boto3.Session(
         #    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
         #    aws_secret_access_key=os.environ.get('AWS_SERVER_ACCESS_KEY')
         # )
         # s3 = session.resource('s3')

         # for AWS remote cloud env
         s3 = boto3.resource('s3')
         s3.meta.client.upload_file(file_path, os.environ.get('S3_BUCKET_NAME'), str(int(round(time.time() * 1000))) + "-" + file_name)
         return 'File uploaded successfully'

@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    form = FileUploadForm(request.form)            

    # Send template information to index.html
    return render_template('index.html', form=form)

app.run(host='0.0.0.0', port=8080, debug=True)