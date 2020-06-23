import mysql.connector as mc
import pandas as pd
import read
from mysql.connector import errorcode as ec

user = "retail_user"
password = "venkatramasai"
host = "34.72.140.44"
db = "retail_db"

connection = mc.connect(user=user,
                        password=password,
                        host=host,
                        database=db
                        )
