from flask import Flask,request

app = Flask(__name__) 

# 接收請求（HTTP Request）
@app.route("/",methods=['GET','POST']) 
def hello_world(): 
  name = request.args.get("name")
  name = request.form.get("name")
  return "<p>hello.html</p>"
  
