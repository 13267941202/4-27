# 定义宏
from flask import Flask, render_template
app = Flask(__name__)


@app.("/")
def index():
    content = {
        "username": "xiaoxie"
    }
    return render_template("macro.html", **content)


if __name__ == '__main__':
    app.run(debug=True, port=8000)