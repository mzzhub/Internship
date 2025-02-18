from flask import Flask, render_template

app = Flask(__name__) # Initializes a new Flask web application

@app.route('/')             # Defines the route for the root URL ('/')
def home():                 # Function that runs when a user visits the root URL
    return "Hello World"    # Returns a simple text response

@app.route('/<name>')                               # Dynamic URL that accepts a 'name' parameter
def temp(name):                                     # Function that renders an HTML template with the given name
    return render_template('doc.html', name_input = name) # Loads and returns 'doc.html' from the templates/ folder

@app.route('/greet/<name>')                 # Another dynamic URL that greets the user by name
def rock(name):                             # Function that returns a personalized greeting
    return"where were you, " + name         # Returns 'Hello' followed by the user's name

@app.route('/<int:age>')                                            # Dynamic URL that accepts an integer 'age' parameter
def military(age):                                                  # Function that checks if the user is allowed based on age
    return "You are not allowed" if age < 18 else "You are allowed" # Returns access permission based on age

if __name__ == '__main__':                          # Ensures the script runs only when executed directly
    app.run(host='0.0.0.0', port=5000, debug=True)  # Runs the Flask application on port 5000 with debug mode enabled