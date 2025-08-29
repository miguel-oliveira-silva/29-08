from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', nome=name)

@app.route('/user/')
def userr():
    return render_template('user.html')

@app.route('/rotainexistente')
def rotainexistente():
    return render_template('404.html')
