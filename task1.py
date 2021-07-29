from flask import Flask,jsonify,render_template,request,make_response,redirect,url_for
import json
import os

PEOPLE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def a():
    return render_template("task1_1.html")

@app.route('/modify', methods=['POST'], strict_slashes=False)
def api_modify():
    if request.method == "POST":
        t = int(request.get_json()["a"])
        print(t)
        t = str(t % 3 + 1)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], "kda"+t+".jpg")
        src = request.get_json()["src"]
        print(src)
        if src == "static\images\kda1.jpg":
            resp = make_response(jsonify(full_filename=full_filename,top=5,left=5,wid=50,hig=50,t=1))
        elif src == "static\images\kda2.jpg":
            resp = make_response(jsonify(full_filename=full_filename,top=50,left=50,wid=50,hig=50,t=2))
        elif src == "static\images\kda2.jpg":
            resp = make_response(jsonify(full_filename=full_filename,top=150,left=150,wid=70,hig=30,t=3))
        else:
            resp = make_response(jsonify(full_filename=full_filename,top=5,left=5,wid=50,hig=50,t=1))
        return resp


if __name__ == '__main__':
    app.run(debug=True)