from flask import Flask, url_for, redirect, request

app = Flask(__name__)


@app.("/login/", methods=["GET", "POST"])
def login():
    return "login"


@app.("/profile/", methods=["GET",  "POST"])
def profile():
    name = request.args.get("name")
    if not name:
        # code指定是永久重定向和暂时重定向
        # return redirect(url_for("login"), code=301)
        return redirect(url_for("/login/"))
    else:
        return name


if __name__ == '__main__':
    app.run(port=8000, debug=True)
