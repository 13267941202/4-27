
# 子域名也是在蓝图中实现的，只是多了subdimain参数, 这个参数要和Windows配置的子域名相同
from flask import Blueprint
cms_bp = Blueprint("cms", __name__, subdomain="cms")


@cms_bp.route("/")
def admin():
    return "cms页面"