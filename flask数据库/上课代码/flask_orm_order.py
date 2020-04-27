# @ Time    : 2020/4/24 20:58
# @ Author  : JuRan

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table


# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0424'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    # create_time = Column()

    # __repr__
    def __str__(self):
        return "Article(title:%s)" % self.title

    # __mapper_args__ = {
    #     # "order_by": id.desc()
    #     "order_by": id
    # }

session = sessionmaker(bind=engine)()

# Base.metadata.drop_all()
Base.metadata.create_all()

# for i in range(10):
#     article = Article(title='title%s' % i)
#     session.add(article)
# session.commit()

# order_by 默认是 升序
# articles = session.query(Article).order_by(Article.id).all()
# 倒叙
# articles = session.query(Article).order_by(Article.id.desc()).all()
# articles = session.query(Article).order_by(-Article.id).all()
# for article in articles:
#     print(article)

# articles = session.query(Article).all()
# for article in articles:
#     print(article)

# 3条数据 前三条数据
# articles = session.query(Article).limit(3).all()

# 查询3-5条数据  offset  从零开始的 偏移量
# articles = session.query(Article).offset(2).limit(3).all()

# articles = session.query(Article).order_by(Article.id.desc()).offset(2).limit(3).all()

# articles = session.query(Article).limit(3).offset(2)
# print(articles)
# for article in articles:
#     print(article)


# 切片
# articles = session.query(Article).all()[2:5]
# print(articles)
# for article in articles:
#     print(article)


