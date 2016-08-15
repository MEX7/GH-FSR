# encoding: utf-8

import pymysql.cursors


class PyMysqlOperate:
    def __init__(self):
        self.connection = pymysql.connect(host='interanjibei.mysql.rds.aliyuncs.com',
                                          user='dbadmin',
                                          password='FDSF2Sccew4gijvlp',
                                          db='anjibei_test',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def cut_data(self, excel_list=None):
        if not excel_list:
            excel_list = []
        i = 0
        for item in excel_list:
            max_user_sid = self.__insert_user(item['user_id'], item['user_nickname'])
            self.__insert_password(item['user_password'], max_user_sid['MAX(user_sid)'])
            i += 1
            print("已导入用户数:"+str(i))
        self.connection.close()

    def __insert_user(self, user_id, user_nickname):
        # Connect to the database
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO t_user (user_id, user_nickname) VALUES (%s, %s)"
                cursor.execute(sql, (user_id, user_nickname))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()

            with self.connection.cursor() as cursor:
                # # Read a single record
                sql = "SELECT MAX(user_sid) FROM t_user"
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            print("user 表写入成功")
        return result

    def __insert_password(self, user_password, user_sid):
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO t_user_key (user_sid, user_password) VALUES (%s, %s)"
                cursor.execute(sql, (user_sid, user_password))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()

        finally:
            print("user_key 表写入成功")