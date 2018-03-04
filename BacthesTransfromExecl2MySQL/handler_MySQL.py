# -*- coding:utf-8 -*-
'''
author: Barnett
'''

import pymysql
from BacthesTransfromExecl2MySQL.config_MySQL import LOCALCONFIG


class HandlerMysql(object):
    def __init__(self, config=None):
        self._config = config
        self._conn = self.__getconn()
        self._cursor = self._conn.cursor()

    def __getconn(self):
        """
        Get connection of MySQL
        :param self: Object HandlerMysql
        :return: connection of MySQL
        """""
        if self._config == None:
            config = LOCALCONFIG
        else:
            config = self._config
        config['cursorclass'] = pymysql.cursors.DictCursor
        conn = pymysql.connect(**config)
        return conn

    def getall(self, sql, param=None):
        row_counts = self.__query(sql, param)
        if row_counts == 0:
            results = []
        else:
            results = self._cursor.fetchall()
        return results

    def getmany(self, sql, param=None):
        row_counts = self.__query(sql, param)
        if row_counts == 0:
            results = []
        else:
            results = self._cursor.fetchmany(row_counts)
        return results

    def getone(self, sql, param=None):
        row_counts = self.__query(sql, param)
        if row_counts == 0:
            results = []
        else:
            results = self._cursor.fetchone()
        return results

    def insertmany(self, sql, values):
        return self._cursor.executemany(sql, values)

    def insertone(self, sql, value):
        return self._cursor.execute(sql,value)

    def update(self, sql, param):
        self._cursor.execute(sql, param=None)

    def delete(self, sql, param=None):
        return self.__query(sql, param)

    def commit(self):
        self._conn.commit()

    def autocommit(self, auto_status=True):
        if auto_status == False:
            self._conn.autocommit_mode = False
        else:
            self._conn.autocommit_mode = True

    def close(self):
        self._cursor.close()
        self._conn.close()

    def reconnect(self):
        self.__init__()

    def change_db(self, new_db):
        """
        Change database of MySQL
        Default database:xinlangfinance
        :param new_db: new database name
        :return: None
        """
        self._conn.select_db(new_db)

    def creat_tb(self, sql, param=None):
        self.__query(sql, param)

    def __query(self, sql, param):
        if param == None:
            row_counts = self._cursor.execute(sql)
        else:
            row_counts = self._cursor.execute(sql, param)
        return row_counts

    def _execute(self, sql):
        self._cursor.execute(sql)


