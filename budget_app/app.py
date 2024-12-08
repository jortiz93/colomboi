# Import required modules
from flask import Flask, render_template

# Initialize flask app(create instance of Flask class)
app = Flask(__name__)

# Define routes(Route in Flask maps URL to a specific fucntion)
@app.route('/')
def hone():
    return "Welcome to the Budget App!"


# TODO add more routes if needed

# Run the application
if __name__ == '__main__':
    app.run(debug=True)