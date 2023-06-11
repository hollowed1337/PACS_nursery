from connect_to_db import connect_to_batabase
from psycopg2.extras import NamedTupleCursor
from datetime import datetime

conn = connect_to_batabase()

def create_log(card_id: int, reader_id):
    try:
        date = datetime.now()
        print(card_id)
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute(f'SELECT id FROM cards WHERE id={card_id}')
            cards = curs.fetchone()
            if cards==None:
                print("Карты с таким ID не существует, введите другое значение")
            else:
                curs.execute(f'SELECT id FROM readers WHERE id={reader_id}')
                reader = curs.fetchone()
                if reader == None:
                    print("Считывателя с таким ID не существует")
                else:
                    curs.execute(f"INSERT INTO logs (id_reader, id_card, date) VALUES ('{reader_id}', '{card_id}', '{date}')")
        conn.commit()

    except Exception as e:
        print(e)
        pass   

while True:
    try:
        print("Введите ID карты")
        dc = int(input())
        print("Введите ID считывателя")
        dr = int(input())
        
        create_log(dc, dr)
        
    except Exception as e:
        print(e)
        pass      