# @ Time    : 2020/4/24 22:01
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
    city = Column(String(50))
    age = Column(Integer)

    def __str__(self):
        return "User(username:%s)" % self.username


# Base.metadata.drop_all()
Base.metadata.create_all()

session = sessionmaker(bind=engine)()


# 查询和李 相同的城市和年龄的人

user = session.query(User).filter(User.username == '李').first()
print(user.city)
print(user.age)
result = session.query(User).filter(User.city == user.city, User.age == user.age).all()
for data in result:
    print(data)

# sub = session.query(User.city.label('city'), User.age.label('age')).filter(User.username == '李').subquery()
# # c column
# result = session.query(User).filter(User.city == sub.c.city, User.age == sub.c.age)
# print(result)
# for data in result:
#     print(data)







