from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker, relationship, backref

USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
PORT = 3306
DATABASE = "flask_db"
db_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(db_url)
Base = declarative_base(engine)
session = sessionmaker(bind=engine)()


# 一对多
# class Classes(Base):
#     __tablename__ = "classes"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     class_name = Column(String(30))
#     # 父表是得到的是对象
#     student_rela = relationship("Students")
#
#     def __str__(self):
#         return "{}: (id:{}, class_name:{})".format(self.__tablename__, self.id, self.class_name)
#
#
# class Students(Base):
#     __tablename__ = "students"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(30))
#     # ondelete是如果父级表数据删除了，子表会设置为空
#     cid = Column(Integer, ForeignKey('classes.id', ondelete="SET NULL"))
#     # 字表可以直接得到relationship的字段数据
#     class_rela = relationship("Classes")
#
#     def __str__(self):
#         return "{}: (id:{}, name:{},cid:{})".format(self.__tablename__, self.id, self.name, self.cid)


# stu = session.query(Students).first()
# print(stu.class_rela)
#
# print(Classes.student_rela)
#
# # 父表
# cla = session.query(Classes).first()
# class_1 = cla.student_rela
# for i in class_1:
#     print(i)
# print(cla.student_rela)
# cla = stu.class_rela
# 添加一条数据
# cla = Classes(class_name="大神班")
# stu = Students(name="治达")
# stu.class_rela = cla
# session.add(stu)
# session.commit()
# 添加多条数据

# 多对多
# 定义中间表
classes1_teachers = Table("classes1_teachers",
                         Base.metadata,
                         Column("classes1_id", Integer, ForeignKey("classes1.id")),
                         Column("teacher", Integer, ForeignKey("teacher.id"))
)


class Classes1(Base):
    __tablename__ = "classes1"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))

    def __str__(self):
        return "{}: (id:{}, name:{})".format(self.__tablename__, self.id, self.name)


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    classes = relationship("Classes1", backref="teachers", secondary=classes1_teachers)

    def __str__(self):
        return "{}: (id:{}, name:{})".format(self.__tablename__, self.id, self.name)


# Base.metadata.create_all()

teacher1 = Teacher(name="juran")
teacher2 = Teacher(name="xiao")
class1 = Classes1(name="高级班")
class2 = Classes1(name="大神班")
teacher1.classes.append(class1)
teacher1.classes.append(class2)
teacher2.classes.append(class1)
teacher2.classes.append(class2)
session.add_all([teacher1, teacher2])
# print(teacher1.classes)
session.commit()

