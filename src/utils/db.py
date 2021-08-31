from dbutils.persistent_db import PersistentDB
import pymysql
import config

pool = PersistentDB(pymysql,
                    maxusage=5,
                    host='localhost',
                    user=config.db_user,
                    passwd=config.db_pwd,
                    db='news',
                    port=3306)
