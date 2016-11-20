__author__ = 'hongliang'
# _*_ coding:utf-8 _*_
import csv
csvfile = file('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['id', 'url', 'keywords'])
data = [
  ('1', 'https://github.com/hongliang5623', '5623'),
  ('2', 'http://www.baidu.com/', '百度'),
  ('3', 'http://www.jd.com/', '京东')
]
writer.writerows(data)
csvfile.close()