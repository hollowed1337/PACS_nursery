from connect_to_db import connect_to_batabase
from psycopg2.extras import NamedTupleCursor

conn = connect_to_batabase()


def get_information_by_card(card_id: int):

    door_id = []
    door_id_card = []
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(f'SELECT * FROM cards WHERE id={card_id}')
        cards = curs.fetchone()
        if cards==None:
            print("Карты с таким ID не существует, введите другое значение")
        else:
            people_id = cards.people_id
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(f"SELECT door_id FROM door_people WHERE people_id={people_id}")
                pd = curs.fetchall()
                for i in range(0, len(pd)):
                    door_id.append(str(pd[i][0]))
                for id in door_id:
                    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                        curs.execute(f"SELECT * FROM doors WHERE id={id}")
                        door = curs.fetchall()
                        door_id_card.append(door[0].id)
        return door_id_card


def get_infornation_by_reader(reader_id: int):

    door_id_reader = []
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(f'SELECT * FROM readers WHERE id={reader_id}')
        reader = curs.fetchone()
        if reader == None:
            print("Считывателя с таким ID не существует")
        else:
            cabinet_id = reader.cabinet_id
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(f"SELECT * FROM doors WHERE cabinet_id={cabinet_id}")
                door = curs.fetchall()
                if door==None:
                    print("Door = None")
                else:
                    for i in range(len(door)):
                        door_id_reader.append(door[i].id)
                print("boba" + str(door_id_reader))
        return door_id_reader


def access(door_id_c, door_id_r):
    ob = []
    if door_id_c != None and door_id_r != None:
        for i in door_id_c:
            for j in door_id_r:
                if i == j:
                    ob.append(i)
        if len(ob)!=0:
            print(f"access is allowed")
        else:
            print(f"access denied")
            return "Нет доступных для открытия дверей"
    else:
        return "Нет доступных для открытия дверей"
    return ob

while True:
    try:
        print("Введите ID карты")
        dc = int(input())
        print("Введите ID считывателя")
        dr = int(input())

        door_id_card = get_information_by_card(dc)
        door_id_reader = get_infornation_by_reader(dr)
        print(access(door_id_card, door_id_reader))
        
    except Exception as e:
        print(e)
        pass        