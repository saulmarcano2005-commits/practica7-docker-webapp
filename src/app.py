from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo Docker + MySQL funcionando"

app.run(host='0.0.0.0',port=5000)
