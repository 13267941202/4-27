# 导入创建引擎方法
from sqlalchemy import create_engine
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "python_test"
# 创建存储引擎
db_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
engine = create_engine(db_url)
# 创建连接
with engine.connect() as con:
    # 执行sql语句
    result = con.execute("select * from students")
    # 显示一条(元组)
    print(result.fetchone())
    # 显示多条（列表）
    print(result.fetchmany(4))
    # 显示全部（列表）
    print(result.fetchall())
