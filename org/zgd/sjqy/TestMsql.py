import pymysql

'''mysql数据库连接'''


# 创建连接mysql的类
class TestMsql:
    # 初始化变量
    def __init__(self, username, host, port, password, database):
        self.username = username
        self.host = host
        self.port = port
        self.password = password
        self.database = database

    # 创建数据库连接
    def connect_mysql(self):
        db = pymysql.connect(user=self.username, host=self.host, port=self.port, passwd=self.password,
                                  database=self.database)
        return db

