from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
@app.route("/index/<name>")
def index(name=None):
    return render_template('index.html', name=name)



@app.route('/upload')
def upload():
    return render_template('upload.html')
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('pagina.html', user_image = f.filename)
        return f.filename
		
		
