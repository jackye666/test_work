from flask import Flask,jsonify,render_template,request,make_response,redirect,url_for
import json
import os
import random
app = Flask(__name__)

@app.route('/')
def a():
    return render_template("task2_2.html")

@app.route('/modify', methods=['POST'], strict_slashes=False)
def modify():
    data1 = random.random()
    data2 = random.random()
    if request.method == 'POST':
        resp = make_response(jsonify(data1=data1,data2=data2))
        return resp
if __name__ == '__main__':
    app.run(debug=True)