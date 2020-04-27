# @ Time    : 2020/4/24 20:36
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

"""
mytable = Table("mytable", metadata,
        Column('mytable_id', Integer, primary_key=True),
        Column('value', String(50))
   )
"""

# 中间表的定义
teacher_classes = Table(
    "teacher_classes",
    Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teacher.id')),
    Column('classes_id', Integer, ForeignKey('classes.id'))
)


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    classes = relationship('Classes', backref='teachers', secondary=teacher_classes)

    def __str__(self):
        return "Teacher(name:%s)" % self.name


class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __str__(self):
        return "Teacher(name:%s)" % self.name


session = sessionmaker(bind=engine)()

# Base.metadata.drop_all()
Base.metadata.create_all()

# teacher1 = Teacher(name='juran')
# teacher2 = Teacher(name='lg')
#
# classes1 = Classes(name='基础班')
# classes2 = Classes(name='进阶班')
#
#
# teacher1.classes.append(classes1)
# teacher1.classes.append(classes2)
#
# teacher2.classes.append(classes1)
# teacher2.classes.append(classes2)
#
# session.add(teacher1)
# session.add(teacher2)
# session.commit()


# 老师对应的班级
# teacher = session.query(Teacher).first()
# print(teacher)
# for i in teacher.classes:
#     print(i)


# 班级对应的老师
# classes = session.query(Classes).first()
# for i in classes.teachers:
#     print(i)





