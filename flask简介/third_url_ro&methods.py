from flask import Flask, url_for, request
app = Flask(__name__)



# @app.("/",)
# def index():
#     print(url_for("action", aid=23))  #url_for 是从函数名获取URL
#     return "xiaoxie"
#
#
# @app.("/action/<aid>")
# def action(aid):
#     return "这是{}页".format(aid)
#
#
# if __name__ == '__main__':
#     app.run(port=8000, debug=True)
#     print(1)

# 指定访问的方法methods
@app.("/login/", methods=["GET", "POST"])
def login():
    # print(request.args.get("username"))  # 接受get访问的参数
    print(request.form.get("name"))  # 接受form访问的参数(body里面的key)
    return "login"


if __name__ == '__main__':
    app.run(debug=True)