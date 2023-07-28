# 导入pymysql模块
import pymysql
# 连接器
import TestMsql as testMysql
# 增删改查类
import CrudMsyql as crudMysql
import json

if __name__ == "__main__":
    # 定义变量
    username = '用户名'
    host = '数据库地址'
    port = 3306
    password = '密码'
    database = '数据库名称'

    # 初始化常量
    merchant_name = "颐禾郡"
    merchant_no = "1330682800403255296"
    village_sql = "select a.id,	a.merchant_no,a.village_no,a.create_time,a.village_name,a.province_name,a.city_name,a.area_name,a.street,a.longitude,a.latitude,a.remark from b_village  a where  a.merchant_no = " + merchant_no
    floor_sql = "select * from b_village  b where b.merchant_no =" + merchant_no
    house_sql = "select * from b_village  b where b.merchant_no =" + merchant_no

try:
    mysql = testMysql.TestMsql(username, host, port, password, database)
    # todo  python文件名.class名->获取示例
    curd = crudMysql.CurdSqlSession(mysql)
    db = mysql.connect_mysql()
    print("\r\nMySQL 连接成功...")
    curd.find_version(db)
    # 查询sql
    querySql = village_sql
    json_str = curd.select_data(db, querySql)
    # json_str = '''
    # [
    #     {"name": "John", "age": 30},
    #     {"name": "Alice", "age": 25},
    #     {"name": "Bob", "age": 35}
    # ]
    # '''
    if json_str:
        # print(json_str)
        '''匹配json对象的node节点数据'''
        # # todo 获取第一个对象
        # parameter_value = json_string[0]
        # # 获取第[几]个对象的某个[字段]值
        # # parameter_value = json_str[1]["name"]
        # print("【json转换后】数据对象:", parameter_value)

        # 将 JSON 字符串解析为 Python 列表
        # json_array = json.loads(json_str)
        # 使用循环遍历 JSON 数组中的对象
        # for obj in json_array:
        #     print("name:", obj["name"])
        #     print("age:", obj["age"])
        #     print("-----------------------")

    # # 新增表使用 execute() 方法执行 SQL，如果表存在则删除
    # drop_sql = "DROP TABLE IF EXISTS EMPLOYEE"
    # # 使用预处理语句创建表
    # create_sql = """CREATE TABLE EMPLOYEE (
    #                  FIRST_NAME  CHAR(20) NOT NULL,
    #                  LAST_NAME  CHAR(20),
    #                  AGE INT,
    #                  SEX CHAR(1),
    #                  INCOME FLOAT )"""
    # curd.create_table(db, drop_sql, create_sql)
    # SQL 插入语句
    # insert_sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
    #                  LAST_NAME, AGE, SEX, INCOME)
    #                  VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
    # curd.insert_mysql(db, insert_sql)
    # SQL 更新语句
    # update_sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    # curd.update_mysql(db, update_sql)
    # 删除表数据
    # delete_sql = "Delete from employee where AGE>%s" % (20)
    # curd.delete_data(db, delete_sql)
    curd.close_mysql(db)
except Exception as e:
    print("Error connecting to MySQL: " + str(e))
except pymysql.err.OperationalError as e:
    print("连接意外断开、 数据库名未找到: " + str(e))
