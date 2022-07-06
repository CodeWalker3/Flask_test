import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="teste",
        user='flaskapi',
        password='123456')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute(
'CREATE TABLE users (id serial PRIMARY KEY,'
'nome varchar (50) NOT NULL,'
'email varchar (50) NOT NULL UNIQUE,'
'password varchar (25) NOT NULL,'
'bairro varchar (25) NOT NULL,'
'rua varchar (25) NOT NULL,'
'numero integer NOT NULL);'
)
cur.execute('DROP TABLE IF EXISTS produto;')
cur.execute(
'CREATE TABLE produto (id serial PRIMARY KEY,'
'nome varchar (50) NOT NULL,'
'preco decimal NOT NULL);'
)

# Insert data into the table

cur.execute('INSERT INTO users (nome, email, password, bairro, rua, numero)'
            'VALUES (%s, %s, %s, %s ,%s ,%s)',
            ('John stuart',
             'jhon@gmail.com',
             '1231564',
             'Toroto',
             'Torrreto',
             123,)
            )


cur.execute('INSERT INTO produto (nome, preco)'
            'VALUES (%s, %s)',
            ('Cardume',
             12.5,)
            )

conn.commit()

cur.close()
conn.close()