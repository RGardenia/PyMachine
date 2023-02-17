import pymysql
from flask import current_app


class MySQL():
    def __init__(self):
        self.conn = pymysql.connect(
            host=current_app.config['DATABASE_HOST'],
            port=current_app.config['DATABASE_PORT'],
            user=current_app.config['DATABASE_USER'],
            passwd=current_app.config['DATABASE_PASSWORD'],
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def create_database(self):
        self.cursor.execute('show databases')
        database_all = self.cursor.fetchall()
        print(database_all)
        num = 0
        for content in database_all:
            if content['Database'] == current_app.config['DATABASE_NAME']:
                num = num + 1
        if num == 0:
            try:
                create_database_sql = f'CREATE DATABASE IF NOT EXISTS {current_app.config["DATABASE_NAME"]} DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
                print(create_database_sql)
                self.cursor.execute(create_database_sql)
            except pymysql.Error as e:
                print('pymysql.Error: ', e.args[0], e.args[1])
            self.create_table()
        else:
            print("数据库已经存在")
        self.closemysql()

    def create_table(self):
        self.cursor.execute(f'use {current_app.config["DATABASE_NAME"]} ;')
        self.cursor.execute('Show tables;')
        table_list_info = self.cursor.fetchall()
        num = 0
        for content in table_list_info:
            if content == current_app.config["DATABASE_TABLE_STUDENT"]:
                num = num + 1
        if num == 0:
            try:
                create_table_sql = f'CREATE TABLE IF NOT EXISTS `{current_app.config["DATABASE_TABLE_STUDENT"]}`(`id` INT UNSIGNED AUTO_INCREMENT,`title` VARCHAR(100) NOT NULL,`author` VARCHAR(40) NOT NULL,`date` DATE,PRIMARY KEY ( `id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;'
                print(create_table_sql)
                self.cursor.execute(create_table_sql)
                create_table_sql2 = f'CREATE TABLE IF NOT EXISTS `{current_app.config["DATABASE_TABLE_TEACHER"]}`(`id` INT UNSIGNED AUTO_INCREMENT,`title` VARCHAR(100) NOT NULL,`author` VARCHAR(40) NOT NULL,`date` DATE,PRIMARY KEY ( `id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;'
                print(create_table_sql2)
                self.cursor.execute(create_table_sql2)
            except pymysql.Error as e:
                print('pymysql.Error: ', e.args[0], e.args[1])
        else:
            print("表已经存在")
        print(table_list_info)

    # 增加,删除,改数据
    def control_data(self, sql):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f'use {current_app.config["DATABASE_NAME"]} ;')
        try:
            result = self.cursor.execute(sql)
            print(result)
        except pymysql.Error as e:
            print('pymysql.Error: ', e.args[0], e.args[1])
        self.closemysql()
        return result

    # 查询数据库
    def select_data(self, sql):
        self.conn.ping(reconnect=True)
        self.cursor.execute(f'use {current_app.config["DATABASE_NAME"]} ;')
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data)
        except pymysql.Error as e:
            print('pymysql.Error: ', e.args[0], e.args[1])
        self.closemysql()
        return data

    # 操作关闭数据库
    def closemysql(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
