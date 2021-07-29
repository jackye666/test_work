from flask import Flask,jsonify,render_template,request,make_response,redirect,url_for

app = Flask(__name__)

@app.route('/')
def a():
    return render_template("test2.html")


if __name__ == '__main__':
    app.run(debug=True)