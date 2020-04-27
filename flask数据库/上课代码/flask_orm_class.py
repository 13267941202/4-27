# @ Time    : 2020/4/24 20:06
# @ Author  : JuRan
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy.orm import relationship, backref


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
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    extend = relationship("UserExtend")


class UserExtend(Base):
    __tablename__ = "user_extend"

    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    # 外键
    uid = Column(Integer, ForeignKey("user.id"))
    # , backref=backref("UserExtend", uselist=False)
    user = relationship("User")


# Base.metadata.drop_all()
Base.metadata.create_all()

session = sessionmaker(bind=engine)()

# user = User(username='juran')
# extend1 = UserExtend(school='lg')
# extend2 = UserExtend(school='lg')
# extend1.user = user
# extend2.user = user
# session.add(extend1)
# session.add(extend2)
# session.commit()

# user.extend.append(extend1)
# user.extend.append(extend2)
#
# session.add(extend1)
# session.add(extend2)
# session.commit()


user = User(username='juran')
extend = UserExtend(school='lg')

extend.user = user

session.add(extend)
session.commit()


















# 社区版
# 专业版
# 代码提示















