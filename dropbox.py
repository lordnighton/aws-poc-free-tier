from flask import Flask, request, render_template
import os
from os import path, getcwd
from os.path import join
from fileUploadForm import FileUploadForm
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['fileUploadField']
      file_name = secure_filename(f.filename)
      file_path = os.path.join(os.getcwd(), file_name)
      print ("File name = " + file_name + ", file path = " + file_path)
      f.save(file_path)
      return 'File uploaded successfully'

@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    # Create form
    form = FileUploadForm(request.form)            

    # Send template information to index.html
    return render_template('index.html', form=form)

app.run(host='0.0.0.0', port=8080, debug=True)