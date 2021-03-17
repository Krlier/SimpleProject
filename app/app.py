#coding: utf-8

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/")
def login():
    return render_template('login_html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
