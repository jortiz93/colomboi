# Import required modules
from flask import Flask, render_template

# Initialize flask app(create instance of Flask class)
app = Flask(__name__)

# Define routes(Route in Flask maps URL to a specific fucntion)
@app.route('/')
def home():
    # Example data
    labels = ['January', 'February', 'March', 'April', 'May']
    data = [10, 20, 15, 25, 30]
    return render_template('home.html', labels=labels, data=data)

@app.route('/add-transaction')
def add_transaction():
    return render_template('add_transaction.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

# TODO add more routes if needed

# Run the application
if __name__ == '__main__':
    app.run(debug=True)