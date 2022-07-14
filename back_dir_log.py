

# from charset_normalizer import from_path
from datetime import date
import datetime

# from sympy import python
from myfile import backup_proj_src

# from_path=r"D:\proj\vue\vue3-zhihu-ts2"
# to_path=r"D:\proj\vue\vue3-zhihu-ts2-back"

# from_path=r"D:\proj\android\verif_code_android"
# to_path=r"D:\proj\android\verif_code_android-out"

# from_path=r"D:\proj\node\egg-demon\egg-demon"
# to_path=r"D:\school\node\big\egg-git-cache"

# from_path=r"D:\proj\vue\git-cache-vue3"
# to_path=r"D:\school\node\big\git-cache-vue3"

# from_path=r"D:\proj\java\mqtt-control"
# to_path=r"D:\proj\java\zhihu-db"

# from_path=r"D:\proj\vue\vue3-zhihu-ts2"
# to_path=r"D:\school\vue\大作业\提交\vue3-zhihu-ts2"

# from_path=r"D:\proj\java\zhihu-db"
# to_path=r"D:\school\vue\大作业\提交\zhihu-db"

# D:\proj\Android\ZlwAudioRecorder>

# from_path=r"D:\proj\Android\ZlwAudioRecorder"
# to_path=r"D:\proj\Android\ZlwAudioRecorder-no-face"



from_path=r"D:\proj\springboot\kinect3"
to_path=r"D:\proj\newfit\newfit-backend"


# from_path=r"D:\proj\cordova\zhihu-cordova"
# to_path=r"D:\school\vue\大作业\提交\zhihu-cordova"


# peewee.ImproperlyConfigured: MySQL driver not installed!
from peewee import *

# 连接数据库
# database = MySQLDatabase('test', user='root', host='localhost', port=3306)
# database = MySQLDatabase('test', user='root',password='123456', host='localhost', port=3306)
host='43.142.150.223'
# host='localhost'
# database = MySQLDatabase('mqtt_control', user='root',password='123456', host=host, port=3306)
database = MySQLDatabase('mqtt_control', user='root',password='123456', host=host, port=3306)
# 43.142.150.223
# back_dir_log
# 定义Person
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = database
# class back_dir_log

# https://blog.csdn.net/weixin_34334744/article/details/91913194
# python 没有 init ，有类变量
class BackDirLog(Model):
    from_path = CharField()
    to_path= CharField()
    time = DateField()
    # id = IntegerField(primary_key=True)
    id = PrimaryKeyField()

    class Meta:
        database = database

backup_proj_src(from_path,to_path)
# 创建表
# Person.create_table()
print("创建表")
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
# backDirLog = BackDirLog(from_path=from_path, to_path=to_path, time= datetime.datetime.now())
now_time=datetime.datetime.now()
print("now_time",now_time)
# backDirLog = BackDirLog.create(from_path=from_path, to_path=to_path, time= datetime.datetime.now())
backDirLog = BackDirLog.create(from_path=from_path, to_path=to_path, time= now_time)
# P=Person.create(name=’name’,sex=’sex’);
# p.save();
# https://www.cnblogs.com/gl1573/p/10380793.html
# https://blog.csdn.net/benben0729/article/details/80530310
print("backDirLog",backDirLog)
print("backDirLog.id",backDirLog.id)
# http://bbs.chinaunix.net/thread-4186552-1-1.html
# backDirLog None
# save
# python new 对象
# backDirLog None
print("save")
backDirLog.save()