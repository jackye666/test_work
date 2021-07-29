from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/index')
def index2():
    return render_template("index.html")   
@app.route('/')
def fig():
    return render_template("test.html")



if __name__ == '__main__':
    app.run(debug=True)