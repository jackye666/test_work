
from flask import Flask,jsonify,render_template,request,make_response,redirect,url_for
import json
import random

app = Flask(__name__)#实例化app对象

@app.route("/")
def a():
   return render_template("index4.html")

@app.route('/modify', methods=['POST'], strict_slashes=False)
def api_modify():
   if request.method == "POST":
      a = random.random()
      resp = make_response(str(a)) # 请求处理成功后，返回'OK'到html中显示
      return resp
   return "111"
 
if __name__ == '__main__':
   app.run(debug=True)
