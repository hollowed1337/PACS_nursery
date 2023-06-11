import psycopg2
#from src.config import DB_NAME, DB_PASSWD, DB_USER, URL
try:
    def connect_to_batabase():
        #conn = psycopg2.connect(f'postgresql://{DB_USER}:{DB_PASSWD}@{URL}:5432/{DB_NAME}') #основная бд
        #conn = psycopg2.connect(f'postgresql://{DB_USER}:{DB_PASSWD}@database:5432/{DB_NAME}') #тестовая бд
        conn = psycopg2.connect(f'postgresql://polienko:dasohdioh1nkz@localhost:5432/nursery')
        return conn
except:
    print('Невозможно подключиться к базе данных')