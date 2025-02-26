from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'uploaded_images'

@app.route('/')
def home():
    return render_template('upload_image.html')

@app.route('/upload', methods = ["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join(app.config["UPLOAD_PATH"], file.filename))
    return f"{file.filename} Uploaded sucessfully"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = True)