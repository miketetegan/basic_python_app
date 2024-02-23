from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Function to connect to the PostgreSQL database
def connect_to_db():
#   try:
        conn = psycopg2.connect(
            dbname="info",
            user="postgres",  # replace with your PostgreSQL username
            password="password",  # replace with your PostgreSQL password
            host="psql",
            port="5432"
        )
        return conn
#    except psycopg2.OperationalError as e:
#        print("Database connection error:", e)
#        create_database()
#        return connect_to_db()

# Function to create the database if it doesn't exist
def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",  # replace with your PostgreSQL username
        password="password",  # replace with your PostgreSQL password
        host="psql",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE DATABASE info")
    conn.close()

# Function to create the table if not exists
def create_table():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS person (id SERIAL PRIMARY KEY, name VARCHAR, age INTEGER)")
    conn.commit()
    conn.close()

# Home page route
@app.route('/')
def home():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

# Add entry route
@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    age = request.form['age']
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
#    create_database()
    create_table()
    app.run(host='0.0.0.0', port=8080, debug=True)
