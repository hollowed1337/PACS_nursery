from connect_to_db import connect_to_batabase
from psycopg2.extras import NamedTupleCursor
from datetime import datetime

conn = connect_to_batabase()

try:
    def create_log(card_id: int, reader_id):
    
        date = datetime.now()
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute(f'SELECT * FROM cards WHERE id={card_id}')
            cards = curs.fetchone()
            if cards==None:
                return f"Карты с ID {card_id} не существует"
            else:
                curs.execute(f'SELECT * FROM readers WHERE id={reader_id}')
                reader = curs.fetchone()
                if reader == None:
                    return f"Считывателя с ID {reader_id} не существует"
                else:
                    curs.execute(f"INSERT INTO logs (id_reader, id_card, date) VALUES ('{reader_id}', '{card_id}', '{date}')")
                    
        conn.commit()
        
except Exception as e:
    print(e)
    
    
while True:
        
    print("Введите ID карты")
    card_id = input()
    print("Введите ID считывателя")
    reader_id = input()

    create_log(card_id, reader_id)

