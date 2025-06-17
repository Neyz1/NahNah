from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__,     template_folder='public',  static_folder='statics' )


# Créer la Table si elle n'existe pas
def init_db():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS utilisateur (
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL 
                   )  
                   ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])


# Récupère les infos du site pour le mettre dans la data.base
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('logs.db')
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO utilisateur (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
        except sqlite3.IntegrityError:
            pass  # Email déjà existant
        conn.close()
        return redirect('/')

    # Sinon (GET), on affiche tous les utilisateurs
    conn = sqlite3.connect('logs.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM utilisateur")
    utilisateurs = cur.fetchall()
    conn.close()
    return render_template('index.html', utilisateurs=utilisateurs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)