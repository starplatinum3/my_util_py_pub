

# from charset_normalizer import from_path
from datetime import date
import datetime
from myfile import backup_proj_src

from_path=r"D:\proj\vue\vue3-zhihu-ts2"
to_path=r"D:\proj\vue\vue3-zhihu-ts2-back"


from peewee import *

# 连接数据库
# database = MySQLDatabase('test', user='root', host='localhost', port=3306)
# database = MySQLDatabase('test', user='root',password='123456', host='localhost', port=3306)
database = MySQLDatabase('mqtt_control', user='root',password='123456', host='localhost', port=3306)
# back_dir_log
# 定义Person
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = database
# class back_dir_log

class BackDirLog(Model):
    from_path = CharField()
    to_path= CharField()
    time = DateField()
    id = IntegerField()

    class Meta:
        database = database

# backup_proj_src(from_path,to_path)
# 创建表
# Person.create_table()
BackDirLog.create_table()
# 创建表也可以这样, 可以创建多个
# database.create_tables([Person])

# https://www.jianshu.com/p/8d1bdd7f4ff5
# 添加一条数据
# p = Person(name='liuchungui', birthday=date(1990, 12, 20), is_relative=True)
# p.save()
# python  现在时间
# now_time = datetime.datetime.now()
# backDirLog = BackDirLog(from_path=from_path, to_path=to_path, time=date())
backDirLog = BackDirLog(from_path=from_path, to_path=to_path, time= datetime.datetime.now())
print("backDirLog",backDirLog)
# backDirLog None
print("save")
backDirLog.save()