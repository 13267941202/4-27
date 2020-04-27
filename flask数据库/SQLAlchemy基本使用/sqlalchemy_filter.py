from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
import random
USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
PORT = 3306
DATABASE = "flask_db"
db_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(db_url)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(30))
    age = Column(Integer)

    def __str__(self):
        return "(id:{}, name:{},age:{})".format(self.id, self.name, self.age)


# Base.metadata.create_all()
# Base.metadata.create_all()
# for i in range(5):
#     user = User(name=random.choices("afhaiof"), age=random.randint(1, 10))
#     session.add(user)
# session.commit()
# 过滤条件
# "="
# result = session.query(User).filter_by(age=6).all()
# "!="
# result = session.query(User).filter(User.age != 6).all()
# “like”  模糊查询
# result = session.query(User).filter(User.name.like("%f%")).all()
# “in”  传入一个列表
# result = session.query(User).filter(User.age.notin_([1])).all()
# “is_null” 空字符串也不算None
# result = session.query(User).filter(User.name.isnot(None)).all()
# “and”  需要导入
# result = session.query(User).filter(and_(User.name.isnot(None), User.age == 1)).all()
# “or”  需要导入
result = session.query(User).filter(or_(User.name.isnot(None), User.age == 1)).all()
for i in result:
    print(i)



