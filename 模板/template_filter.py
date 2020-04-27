from flask import Flask, render_template
app = Flask(__name__)
from datetime import datetime

@app.("/")
def index():
    content = {
        "username": "juran  nishi",
        "age": -18,
        "EnglishName": "XCAIYUAN",
        "name": "difaxie",
        "books": ["python", "java"],
        "dic": "hello world",
        "es": "<script>alert(123);</script>",
        "brackets": "<h1>这是去标签</h1>",
        "time": datetime(2020, 4, 12, 1, 6, 00)
    }
    return render_template("template_filter.html", **content)


# 自定义过滤器
@app.template_filter("mycut")
def cut(value):
    return value.replace("nishi", "nihao")


@app.template_filter("headle_time")
def get_time(time):
    """
    time小于一分钟->刚刚
    time大于一分钟小于一个小时->xx分钟之前
    time大于一个小时小于24小时->xx小时之前
    """

    if isinstance(time, datetime):
        # total_seconds获取总秒数
        report_time = (datetime.now() - time).total_seconds()
        if report_time < 60:
            return "刚刚"
        elif 60 <= report_time < 60*60:
            return "{}分钟之前".format(int(report_time/60))
        elif 60*60 <= report_time < 60*60*24:
            return "{}小时之前".format(int(report_time/(60*60)))
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True, port=8000)