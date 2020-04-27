from flask import Flask
# 传入__name__初始化一个Flask实例
app = Flask(__name__)


# app.装饰器映射URL和执行的函数。这个设置将根URL映射到了hello_world函数上
@app.('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 通过对象
    # app.debug = True
    # 通过参数
    # debug=True
    # 通过配置项来开启debug
    app.config.update(DEBUG=True)
    app.run()

# 配置文件

# from flask import Flask
# # 导入配置文件
# # import setting
# # import setting1
#
# app = Flask(__name__)
# app.("/")
#
#
# def hello_xiao():
#     return "hello xiaoxie"
#
#
# if __name__ == '__main__':
#     # 直接硬编码 缺点是写死了，需要修改的时候不方便
#     # app.config["DEBUG"] = True
#     # 通过update方法  app.config 是继承dict类，是一个字典
#     # app.config.update(DEBUG=True)
#     # 通过我们自己创建一个配置文件，里面存储配置(只限py后缀文件)
#     # app.config.from_object(setting)
#     # app.config.from_object("setting")
#     # 也是通过导入文件（不仅仅限于py文件，都是必须写完整的文件名）,silent 是导入错误可以控制是否报错，默认是会
#     app.config.from_pyfile("seetting1.ini", silent=True)
#
#     app.run()