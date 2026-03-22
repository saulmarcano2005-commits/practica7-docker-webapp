from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo Docker + MySQL"

app.run(host='0.0.0.0',port=5000)from flask import Flask

