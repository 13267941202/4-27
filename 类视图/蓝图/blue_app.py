from flask import Flask, render_template, url_for
# 导入蓝图
from blueprints.book import book_bp
from blueprints.news import news_bp
# 子域名
from blueprints.sumdomain_bp import cms_bp


app = Flask(__name__)

app.config["SERVER_NAME"] = "xiaoxie.com:8899"

# 注册蓝图中的url
app.register_blueprint(book_bp)
app.register_blueprint(news_bp)
#子域名注册
app.register_blueprint(cms_bp)


@app.route("/")
def index():
    # 使用url_for 也是一样，要加上蓝图名字
    # print(url_for("book.book"))
    return "nihao"


if __name__ == '__main__':
    app.run(debug=True, port=8899)