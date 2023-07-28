# mysql数据库操作crud
import json


class CurdSqlSession:
    def __init__(self, db):
        self.db = db

    # 查询数据库的版本
    def find_version(self, db):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print("数据库版本: %s " % data)

    def select_data(self, db, querySql):
        try:
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(querySql)
            # 使用 fetchone() 方法获取单条数据.
            result = cursor.fetchall()
            keys = [desc[0] for desc in cursor.description]
            json_data = [{keys[i]: row[i] for i in range(len(keys))} for row in result]
            # todo ensure_ascii 代表不转义
            json_str = json.dumps(json_data, indent=4, ensure_ascii=False)
            print(json_str)
            # 输出结果
            # for row in result:
            #     print(row)
            # 关闭游标和连接
            cursor.close()
            return json_str
        except Exception as e:
            print(e)

    # 新增数据表
    def create_table(self, db, dropTableSQL, insertTableSql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        cursor.execute(dropTableSQL)
        # 使用预处理语句创建表
        cursor.execute("" + insertTableSql + "")
        print("新增成功！！！！")

    # 数据库的插入操作
    def insert_mysql(self, db, insertSql):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
        #          LAST_NAME, AGE, SEX, INCOME)
        #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
            # 执行sql语句
            cursor.execute(insertSql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        print("插入成功！！！！")

    # 数据库更新操作
    def update_mysql(self, db, updateSql):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        # sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        try:
            # 执行SQL语句
            cursor.execute(updateSql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        print("更新成功！！！")

    # 数据库删除操作
    def delete_data(self, db, deleteSql):
        # 使用cursor() 方法获取操作游标
        cursor = db.cursor()
        # SQL删除语句
        # sql = "Delete from employee where AGE>%s" % (20)
        try:
            # 执行SQL语句
            cursor.execute(deleteSql)
            # 提交修改
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        print("删除成功！！！")

    # 关闭数据库的提示信息
    def close_mysql(self, db):
        # 关闭数据库连接
        db.close()
        print("关闭数据库连接，释放资源")
