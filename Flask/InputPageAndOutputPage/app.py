from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("input_page.html")

@app.route ('/register', methods = ['GET'])
def register():
    name = request.args.get("name_input")
    number = request.args.get("number_input")
    email =  request.args.get("email_input")
    return render_template('output_paragraph_page.html', name_input = name, number_input = number, email_input = email)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)