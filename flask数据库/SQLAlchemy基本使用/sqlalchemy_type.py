from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String,  Enum,  DECIMAL, Float, DateTime, Date, Time
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime
from sqlalchemy import func
USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
PORT = 3306
DATABASE = "python_test"
# 创建引擎
db_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(db_URL)

Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Organ(Base):
    __tablename__ = "Organ"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    gender = Column(Enum("男", "女"), nullable=False, default="男")
    # Float不够精确，只会保留3位小数
    # height = Column(Float)
    # DECIMAL可以指定小数位数，第一个参数是一共几位，第二个参数是小数位数
    height = Column(DECIMAL(15, 8))
    join_time = Column(DateTime)
    # LONGTEXT 长文本
    content = Column(LONGTEXT)
    update_time = Column(DateTime, onupdate=datetime.now())


# 删除表
# Base.metadata.drop_all()
# 映射到数据库中，（创建表）
# Base.metadata.create_all()
# user = Organ(name="xie", age=125, gender="女", height="184.47144674",
#              join_time=datetime(2020, 4, 22, 16, 25, 45), content="dfihf")
# update_data = session.query(Organ).first()
# session.add(user)
# session.commit()

# 聚合函数
result = session.query(func.max(Organ.age)).first()
result1 = session.query(func.min(Organ.age)).first()
result2 = session.query(func.sum(Organ.age)).first()
result3 = session.query(func.avg(Organ.age)).first()
result4 = session.query(func.count(Organ.id)).first()
print(result, result1, result2, result3, result4)
1





