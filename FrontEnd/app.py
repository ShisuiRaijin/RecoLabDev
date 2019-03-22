from flask import Flask, render_template
from flask_restful import Api
from BackEnd.router.Router import Router

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template()

@app.route('/')
def index():
    return render_template()

@app.route('/')
def index():
    return render_template()

@app.route('/')
def index():
    return render_template()

@app.route('/')
def index():
    return render_template()

if __name__ == '__main__':
    app.run(debug=True)
