__author__ = 'MEX'
# -*- coding: utf-8 -*-
import xdrlib, sys
import xlrd
import hashlib


def open_excel(excel_file='info.xls'):
    try:
        data = xlrd.open_workbook(excel_file, encoding_override='utf-8')
        return data
    except Exception, e:
        print str(e)


def excel_table_by_index(colnameindex=0, by_index=0):
    data = open_excel()
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def assemble():
    tables = excel_table_by_index()

    list = []
    for row in tables:
        line = {}
        line['user_nickname'] = row[u' 网名']
        line['user_id'] = row[u' 电话'][0:11]
        m = hashlib.md5()
        m.update("1314520")
        line['user_password'] = m.hexdigest()
        print line
        list.append(line)
    return list
