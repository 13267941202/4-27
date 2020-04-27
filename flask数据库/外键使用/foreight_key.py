from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker, relationship

USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
PORT = 3306
DATABASE = "flask_db"
db_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(db_url)
Base = declarative_base(engine)
session = sessionmaker(bind=engine)()


class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(30))
    student = relationship("Students")

    def __str__(self):
        return "{}: (id:{}, class_name:{})".format(self.__tablename__, self.id, self.class_name)


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    cid = Column(Integer, ForeignKey('classes.id', ondelete="SET NULL"))
    class_rela = relationship("Classes")

    def __str__(self):
        return "{}: (id:{}, name:{},cid:{})".format(self.__tablename__, self.id, self.name, self.cid)


# Base.metadata.drop_all()
# Base.metadata.create_all()
# class1 = Classes(class_name="基础班")
# class2 = Classes(class_name="高级班")
# class3 = Classes(class_name="进阶班")
# student1 = Students(name="xia", cid=2)
# session.add_all([class3])

# stu = session.query(Classes).filter(Classes.id == 2).first()
# 外键查询
# cla = session.query(Classes).filter(Students.cid == Classes.id).first()
# session.delete(stu)
# session.commit()
# print(cla)
# 一对多