# encoding: utf-8
import ExcelOperate
import PyMysqlOperate


def excel2mysql():
    excel_list = ExcelOperate.assemble()
    insert_mysql = PyMysqlOperate.PyMysqlOperate()
    insert_mysql.cut_data(excel_list)


class PyExcelKits:
    def __init__(self):
        pass


test = PyExcelKits()
excel2mysql()