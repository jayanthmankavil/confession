
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('confessions.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS confessions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, reciever TEXT, confession TEXT)''')
    return conn

@app.route('/')
def index():
    conn = get_db()
    confessions = conn.execute("SELECT * FROM confessions").fetchall()
    conn.close()
    return render_template('viewconfession.html', confessions=confessions)

@app.route('/confessions', methods=['POST'])
def submit_confession():
    fr = request.form.get('sender')
    to = request.form.get('reciever')
    confession = request.form.get('confession')

    conn = get_db()
    conn.execute("INSERT INTO confessions (sender, reciever, confession) VALUES (?, ?, ?)", (fr, to, confession))
    conn.commit()
    conn.close()

    return 'Confession submitted successfully!'

if __name__ == '__main__':
    app.run(port=8000)
