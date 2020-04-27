# @ Time    : 2020/4/24 21:37
# @ Author  : JuRan
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker

# localhost
HOSTNAME = '127.0.0.1'
DATABASE = 'demo0424'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(DB_URL)

Base = declarative_base(engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    gender = Column(Enum('男', '女'))
    age = Column(Integer)


# Base.metadata.drop_all()
# Base.metadata.create_all()
session = sessionmaker(bind=engine)()

# import random
# for x in range(10):
#     user = User(username='juran%s' % x, gender='男', age=random.randint(12, 26))
#     session.add(user)
#
# session.commit()

# 按照性别来进行分组, 求男女的人数
# 聚合函数  一般会和分组进行使用
from sqlalchemy import func
# result = session.query(User.gender, func.count(User.id)).group_by(User.gender).all()
# print(result)

# having
# result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 18).all()
# print(result)