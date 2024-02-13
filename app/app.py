#coding: utf-8

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
#My features added here: http://stackoverflow.com/questions/
#Some important features added here: http://stackoverflow.com/questions/
