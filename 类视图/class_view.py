from flask import Flask, render_template, request, url_for, views, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    # 如果加上endpoint参数的话，相当于给映射的函数换一个名字，url_for 反转的时是用endpoint的
    # print(url_for("ceshi"))
    return "首页"


"""
def profile():
    return "个人中心"


class Personview(views.View):

    # 类视图这个方法一定要重写
    def dispatch_request(self):
        return "nihao "

    def demo(self):
        return "hello"


# 返回Json数据（标准类视图）
class JsonView(views.View):
    def get_json(self):
        raise NotImplementedError()

    def dispatch_request(self):
        response = self.get_json()
        return jsonify(response)


# 继承JsonView 不需要重写dispatch_request,但是要重写get_json
class Listjsonview(JsonView):
    def get_json(self):
        return {"username": "xiao"}


# 测试
class Demo(views.View):
    def __init__(self):
        super().__init__()


class Demo1(Demo):
    def dispatch_request(self):
        return "nishi"


# 返回公共变量（标准类视图）
class Baseview(views.View):   # 公共变量部分
    def __init__(self):
        super().__init__()
        self.content = {
            "username": "xiao"
        }


class LoginView(Baseview):  # 登录页面
    def dispatch_request(self):
        return render_template("login.html", **self.content)


class RegisView(Baseview):  # 注册页面
    def dispatch_request(self):
        return render_template("regis.html", **self.content)


# 测试
app.add_url_rule("/demo1/", view_func=Demo1.as_view("demo1"))
# 第一个是路由，如果传入endpoint会优先
app.add_url_rule("/profile/", endpoint="ceshi", view_func=profile)
# as_view也是相当于给函数起了一个名字，使用url_for 时优先用endpoint的
app.add_url_rule("/view/", view_func=Personview.as_view("personview"))
# 返回普通字符串
# app.add_url_rule("/pul/", view_func=JsonView.as_view("pul"))
# 返回Json数据
app.add_url_rule("/Jsonview/", view_func=Listjsonview.as_view("Jsonview"))
# 登录页面
app.add_url_rule("/loginview/", view_func=LoginView.as_view("loginview"))
# 注册页面
app.add_url_rule("/regisview/", view_func=RegisView.as_view("regisview"))
"""

"""
# 基于方法类视图，导入的是MethodView，
class Loginview(views.MethodView):
    # 错误信息也是在登录页面显示的，
    def get(self, error=None):
        return render_template("login.html", error=error)

    def post(self):
        # 接受form表单的数据
        username = request.form.get("username")
        password = request.form.get("password")
        # 模拟查询数据库
        if username == "xiao" and password == "123":
            return "登录成功"
        else:
            return self.get("账号密码错误")


app.add_url_rule("/login/", view_func=Loginview.as_view("login"))
"""

# 函数里面
# 验证装饰器


def loginview(func):
    def wrapper(*args, **kwargs):
        # 接受url传过来的？username形式的参数
        username = request.args.get("username")
        if username:
            return func(*args, **kwargs)
        else:
            return "请先登录"
    return wrapper


# 类里面
class Login(views.View):
    # 类里面使用装饰器
    decorators = [loginview]

    def dispatch_request(self):
        return "个人中心"


app.add_url_rule("/profile/", view_func=Login.as_view("profile"))
# 验证后才可以设置个人中心


@app.route("/setting/")
# 这个装饰器一定要写在后面
@loginview
def profile():
    return "个人设置"


if __name__ == '__main__':
    app.run(debug=True, port=8888)
