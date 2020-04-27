from flask import Flask, render_template

# 指定模板文件查找路径 template_folder
app = Flask(__name__, template_folder=r"D:\flask项目\模板\templates")


# template的模板文件
@app.("/")
def index():
    content = {
        "username": "逻辑教育",
        "num": 11,
        # 字典嵌套字典
        # "books": {
        #     "Python": 23,
        #     "Java": 13
        # },
        # "book": ["Python", "Java", "PHP"]
    }
    # 直接传参的方法
    # return render_template("index.html", username="逻辑教育", age=18)
    # 这样是通过字典传参，但是模板文件会变得冗余
    return render_template("index.html", content=content)
    # **content 会自动把字典转换成username=“”这种形式
    # return render_template("index.html", **content)
# 这是template下面的模板文件
# @app.("/profiles/")
# def profiles():
#     return render_template("/demo/user.html")


if __name__ == '__main__':
    app.run(port=8000, debug=True)