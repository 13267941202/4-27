from flask import Flask, render_template

app = Flask(__name__)


@app.("/")
def index():
    return render_template("include_demo.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
