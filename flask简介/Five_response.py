from flask import Flask, request, make_response, Response

app = Flask(__name__)


@app.("/")
def index():
    # 返回一个字符串
    # return "juran"
    # 返回一个元组
    # return "关于我们", 200
    # 返回一个字典
    return {"username": "xeioa"}
    # 返回一个Response对象
    # return Response("not found", status=404, content_type="text/html")
    # 返回一个make_response对象
    # return make_response("关于我们")


if __name__ == '__main__':
    app.run(port=8000, debug=True)