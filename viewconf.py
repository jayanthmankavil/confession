from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('confessions.db')
    return conn

@app.route('/')
def index():
    conn = get_db()
    confessions = conn.execute("SELECT * FROM confessions").fetchall()
    return render_template('viewconfession.html', confessions=confessions)

if __name__ == '__main__':
    app.run(debug=True)
