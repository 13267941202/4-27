from flask import Flask, render_template
from sqlalchemy import create_engine        # 创建引擎
from sqlalchemy import Column               # 字段
from sqlalchemy import String, Integer      # 数据类型
from sqlalchemy.orm import sessionmaker     # 添加数据需要的

from sqlalchemy.ext.declarative import declarative_base


HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "python_test"
# 创建引擎
ROM_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
engine = create_engine(ROM_URL)
Base = declarative_base(engine)


# 所有的类都要继承declarative_base的实例
class SqlORM(Base):
    # 定义表名
    __tablename__ = "users"
    # 定义字段
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    gender = Column(Integer, default=1, comment="1为男， 2为女")


# 模型映射到数据库中（执行完这条代码数据库就有users这张表了，后续可以把这条代码注释了）
# Base.metadata.create_all()
# 添加数据
Session = sessionmaker(bind=engine)
session = Session()
s = SqlORM(name="小谢")
# 添加到内存中但是还没有提交到数据库中
session.add(s)
# 提交到数据库中
session.commit()
print(s.name)
print(s.id)
