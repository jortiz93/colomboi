# Import required modules
from flask import Flask, render_template, request

# Initialize flask app(create instance of Flask class)
app = Flask(__name__)

# Global variables for persistent data (for development use only)
labels = []
data = []

@app.route('/')
def home():
    return render_template('home.html', labels=labels, data=data)

# Define routes(Route in Flask maps URL to a specific fucntion)
@app.route('/submit', methods=['POST'])
def input():
    error_message = None

    if request.method == 'POST':
        income = request.form.get('income')

        # Validate income
        if income and income.strip():
            try:
                income = float(income)
            except ValueError:
                income = 0  # Default to 0 if invalid
                error_message = "Please enter a valid income."

        else:
            income = 0  # Default to 0 if missing or empty
            error_message = "Income field cannot be empty."

        if not error_message:
            # Add data to labels and data for dynamic updates
            data.append(income)
            labels.append("Income")

    return render_template('home.html', labels=labels, data=data, error_message=error_message)

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