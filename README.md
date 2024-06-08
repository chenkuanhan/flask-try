# flask

# **快速上手**

## **一个最小的应用**

```python
# pip install flask

from flask import Flask

app = Flask(__name__) # 定義一個 Flask 物件 = app 
                      # 基於 app Flask 物件進行不同的設定跟操作
                      # 例如：路由、樣板 ...

@app.route("/") # 當收到網址 `/` 請求時，進入這個路由
def hello_world():
    return "<p>Hello, World!</p>"
```

```python
from flask import Flask,request

app = Flask(__name__) 

# 接收請求（HTTP Request）
@app.route("/",methods=['GET','POST']) 
def hello_world(): 
  name = request.args.get("name")
  name = request.form.get("name")
  return "<p>hello.html</p>"
```

---


```
PS C:\Users\Asus\Documents\ignore_try> git add .
warning: in the working copy of 'hello.py', LF will be replaced by CRLF the next time Git touches it
PS C:\Users\Asus\Documents\ignore_try> git status
On branch master
Your branch is up to date with 'origin/master'.
```

## cheat sheet

1. copy .venv file
2. copy .git file
3. pip install flask
4. pip install Flask
5. flask --app app run
6. flask run
7.  python -m flask --app <filename> run
   
