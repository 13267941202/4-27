from flask import Blueprint, render_template
# url_prefix 是url前缀，如果写了这个，后面route定义url规则的时候就不需要了，但是url_prefix的参数一定是/开头，route还是要写一个/线
# static_folder是指定静态文件夹，但是优先还是会在static里面找
# template_folder是指定模板文件夹，但是优先还是会在templates里面找
book_bp = Blueprint("book", __name__, url_prefix="/book", static_folder="blueprints\\static")


@book_bp.route("/")
def book():
    return render_template("book.html")