import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='teste',
                            user='flaskapi',
                            password='123456')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM produto;')
    produto = cur.fetchall()
    cur.close()
    conn.close()    
    return render_template('index.html', produto=produto)
# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO produto (nome, preco)'
                    'VALUES (%s, %s)',
                    (nome,preco))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('create.html')