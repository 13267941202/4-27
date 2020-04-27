from flask import Blueprint
news_bp = Blueprint("news", __name__)


@news_bp.route("/news/")
def book():
    return "这是蓝图中的news"