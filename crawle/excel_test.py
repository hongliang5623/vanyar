# -*- coding: utf-8 -*-
import xlwt
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'

def export_excel():
    subject_file = xlwt.Workbook()
    subject_table = subject_file.add_sheet(u'测试excel', cell_overwrite_ok=True)
    subject_table.write(0, 0, u'ID')
    subject_table.write(0, 1, u'名字')
    subject_table.write(0, 2, u'url')
    subject_table.write(0, 3, u'内容')
    subject_table.write(0, 4, u'创建时间')
    num = 0
    for count in xrange(10):
        subject_table.write(num, 0, '1001'.decode('utf-8'))
        subject_table.write(num, 1, 'zhangsan'.decode('utf-8'))
        subject_table.write(num, 2, 'https://github.com/hongliang5623')
        subject_table.write(num, 3, 'growing strong')
        subject_table.write(num, 4, time.strftime(ISOTIMEFORMAT, time.localtime() ))
    subject_file.save('test.xls')


if __name__ == '__main__':
    export_excel()
    print 'done....'