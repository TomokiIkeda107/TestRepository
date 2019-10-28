#%%
# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,Flask!!!"

@app.route("/index") #HTMLレンダーバージョン
def index():
    name = "Hello,Flask&HTML!!!"
    return render_template('index.html', message=name) 

## おまじない
if __name__ == "__main__":
    app.run() 


#%%
