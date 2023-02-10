from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('confessions.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS confessions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, confession TEXT)''')
    return conn

@app.route('/confessions', methods=['POST'])
def submit_confession():
    name = request.form.get('name')
    confession = request.form.get('confession')
    
    conn = get_db()
    conn.execute("INSERT INTO confessions (name, confession) VALUES (?, ?)", (name, confession))
    conn.commit()
    conn.close()
    
    return 'Confession submitted successfully!'

if __name__ == '__main__':
    app.run(debug=False)
