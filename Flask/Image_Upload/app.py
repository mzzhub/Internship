from flask import Flask, render_template, request
import os

app = Flask(__name__)   # Create a Flask web application instance

@app.route('/')         # Define route for the home page
def index():
    return render_template("page.html")   # Render the input page when visiting the home page

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files('file')
    file.save(os.path.join(app.config['UPLOAD_PATH']))

if __name__ == '__main__':  # Ensure the script runs only if executed directly
    app.run(host = '0.0.0.0', port = 5000, debug = True)  # Start the Flask web server on port 5000 with debug mode enabled
