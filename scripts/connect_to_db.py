import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2
DB_USER = os.getenv('DB_USER')
DB_PASSWD = os.getenv('DB_PASSWD')
DB_NAME = os.getenv('DB_NAME')
URL = os.getenv('URL')
try:
    def connect_to_batabase():
        #conn = psycopg2.connect(f'postgresql://{DB_USER}:{DB_PASSWD}@{URL}:5432/{DB_NAME}') #основная бд
        conn = psycopg2.connect(f'postgresql://{DB_USER}:{DB_PASSWD}@database:5432/{DB_NAME}') #тестовая бд
        return conn
except:
    print('Невозможно подключиться к базе данных')
