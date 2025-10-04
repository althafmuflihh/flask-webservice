from flask import Flask, request, render_template_string
import pyodbc

app = Flask(__name__)

# 🧠 SQL Server connection details
server = 'localhost\\SQLEXPRESS'
database = 'MyFinance'
username = 'sa'       # replace with your username
password = 'yourpassword'
driver = '{ODBC Driver 17 for SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        description = request.form['description']
        amount = request.form['amount']

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Transactions (date, description, amount) VALUES (?, ?, ?)", (date, description, amount))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Data inserted successfully!'

    return render_template_string('''
        <h2>Insert Transaction</h2>
        <form method="POST">
            Date: <input type="date" name="date" required><br><br>
            Description: <input type="text" name="description" required><br><br>
            Amount: <input type="number" step="0.01" name="amount" required><br><br>
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
