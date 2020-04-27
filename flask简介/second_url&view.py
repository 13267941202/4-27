from flask import Flask
from flask import request
app = Flask(__name__)


# @app.("/list/<aid>/")
# # 函数里面一般是接受加括号里面的，默认是接受字符串
# def hello_xiao(aid):
#     return "string--第一个flask的第{}页".format(aid)

# int
# @app.("/list/<int:aid>")
# def hello_nihao(aid):
#     return "int--第一个flask的第{}页".format(aid)


# path
# @app.("/list/<path:aid>")
# def hello_path(aid):
#     return "path--第一个flask的第{}页".format(aid)


# any
# @app.("/<any(blog,action):url_path>/")
# def hello_ni(url_path):
#     return url_path


# ?name=python

@app.("/wd")
def baidu():
    return request.args.get("name")


if __name__ == '__main__':
    app.run()