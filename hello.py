# pip install flask

from flask import Flask

app = Flask(__name__) # 定義一個 Flask 物件 = app 
                      # 基於 app Flask 物件進行不同的設定跟操作
                      # 例如：路由、樣板 ...

@app.route("/") # 當收到網址 `/` 請求時，進入這個路由
def hello_world():
    return "<p>Hello, World!</p>"