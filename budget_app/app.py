# Import required modules
from flask import Flask, render_template, request

# Initialize flask app(create instance of Flask class)
app = Flask(__name__)

# Global variables for persistent data (for development use only)
labels = []
data = []
income = 0

@app.route('/')
def home():
    return render_template('home.html', labels=labels, data=data)

# Define routes(Route in Flask maps URL to a specific fucntion)
@app.route('/submit', methods=['POST'])
def input():
    global income
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

# Global variable to store transactions
transactions = []

@app.route('/add-transaction', methods=['GET', 'POST'])
def add_transaction():
    global income
    if request.method == 'POST':
        category = request.form.get('category')
        amount = request.form.get('spending')

        # Validate amount
        if amount and amount.strip():
            try:
                amount = float(amount)
            except ValueError:
                amount = 0  # Default to 0 if invalid
        else:
            amount = 0  # Default to 0 if missing or empty

        # Add transaction if valid
        if category and amount > 0:
            transactions.append({'category': category, 'amount': amount})

    # Calculate net amount as income minus the total transactions
    total_spent = sum(item['amount'] for item in transactions)
    net_amount = income - total_spent

    # Pass transactions and net amount to the template
    return render_template('add_transaction.html', transactions=transactions, net_amount=net_amount)

@app.route('/summary')
def summary():
    return render_template('summary.html')

# TODO add more routes if needed

# Run the application
if __name__ == '__main__':
    app.run(debug=True)