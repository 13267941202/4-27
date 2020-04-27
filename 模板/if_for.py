from flask import Flask, render_template

app = Flask(__name__)
@app.("/")
def index():
    content = {
        "username": "xiaoxie",
        "books": ["Python", "Java", "PHP"],
        "users": {
            "name": "xiaoxie",
            "age": 20,
            "high": 170
        }
    }
    return render_template("if_for_template.html", **content)


if __name__ == '__main__':
    app.run(debug=True, port=8000)