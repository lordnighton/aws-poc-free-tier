from flask import Flask, request, render_template
from fileUploadForm import FileUploadForm

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    """Home page of app with form"""
    # Create form
    form = FileUploadForm(request.form)

    # Send template information to index.html
    return render_template('index.html', form=form)

app.run(host='0.0.0.0', port=8080)