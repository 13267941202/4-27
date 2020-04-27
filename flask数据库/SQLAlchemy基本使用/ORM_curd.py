from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import sessionmaker

HOST = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "python_test"
db_url = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(db_url)
Base = declarative_base(engine)


class Books(Base):
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)

    def __str__(self):
        return "(id:{}, name:{}, price:{})".format(self.id, self.name, self.price)


# Base.metadata.create_all()
Session = sessionmaker(bind=engine)
session = Session()

r = session.query(Books).first()
print(r)

def add_data():
    """
    添加一条数据：add
    添加多条：add_all()传入一个列表
    :return:
    """
    book1 = Books(name="Python", price=39)
    book2 = Books(name="平凡的世界", price=99)
    book3 = Books(name="活着", price=89)
    # 添加一条
    # session.add(book1)
    # 添加多条
    session.add_all([book2, book3])
    session.commit()


def search_data(id=None, name=None):
    # 查询表的全部数据
    # search = session.query(Books)
    # 加上判断条件（filter）， 相当与where， 参数使用==好的方式，前面也是加上类名
    # search = session.query(Books).filter(Books.name == "活着")
    # (filter_by)参数是用=号的方式来查询
    search1 = session.query(Books).filter_by(name=name)
    search2 = session.query(Books).filter_by(id=id)

    # first（）
    # search3 = session.query(Books).first()
    # print(search3)

    # all()
    search4 = session.query(Books).all()
    for i in search4:
        print(i)
    # 根据传入的字段来进行查询
    if name is not None:
        for item in search1:
            print(item)
    elif id is not None:
        for item in search2:
            print(item)


def updata_data():
    book_name = session.query(Books).first()
    book_name.name = "Py"
    # for i in book_name:
    #     i.name = "活着"
    # 回滚，修改的操作都是在事务中进行的，如果操作失败应该要回到原始的状态，需要在提交之前进行回滚
    # session.rollback()
    session.commit()


def delete_data():
    # 直接删除(物理删除)
    # del_data = session.query(Books).filter(Books.id == 5)
    # for i in del_data:
    #     session.delete(i)
    # 逻辑删除，其实就是新建一个字段来记录
    session.commit()


if __name__ == '__main__':
    # add_data()
    search_data()
    # updata_data()
    # delete_data()