#%%
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    name = "Hello,Flask!!!"
    # return name
    return render_template('layout.html', name=name) #HTMLレンダーバージョン

## おまじない
if __name__ == "__main__":
    app.run(debug=True) 
