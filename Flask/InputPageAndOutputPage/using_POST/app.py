# Why Use POST Instead of GET?
# ✅ More Secure: Data is not exposed in the URL.
# ✅ Handles Larger Data: Suitable for form submissions.
# ✅ Better for Sensitive Data: Useful for passwords and private information.

from flask import Flask, render_template, request

app = Flask(__name__)   # Create a Flask web application instance

@app.route('/')         # Define route for the home page
def index():
    return render_template("input_page.html")   # Render the input page when visiting the home page

@app.route('/register', methods = ['POST'])  # Define route for handling registration data
def register():
    name = request.form.get("name_input")       # Get the 'name_input' parameter from the GET request
    number = request.form.get("number_input")   # Get the 'number_input' parameter from the GET request
    email = request.form.get("email_input")     # Get the 'email_input' parameter from the GET request
    return render_template('output_paragraph_page.html', name_input = name, number_input = number, email_input = email)  # Render the output page with user data

if __name__ == '__main__':  # Ensure the script runs only if executed directly
    app.run(host = '0.0.0.0', port = 5000, debug = True)  # Start the Flask web server on port 5000 with debug mode enabled
