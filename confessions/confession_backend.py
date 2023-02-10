
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('confessions.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS confessions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, from TEXT,to TEXT, confession TEXT)''')
    return conn

@app.route('/')
def index():
    conn = get_db()
    confessions = conn.execute("SELECT * FROM confessions").fetchall()
    return render_template('viewconfession.html', confessions=confessions)

@app.route('/confessions', methods=['POST'])
def submit_confession():
    f = request.form.get('from')
    to = request.form.get('to')
    confession = request.form.get('confession')

    conn = get_db()
    conn.execute("INSERT INTO confessions (from, to, confession) VALUES (?, ?, ?)", (f, to, confession))
    conn.commit()
    conn.close()

    return 'Confession submitted successfully!'
