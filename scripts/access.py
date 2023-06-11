from connect_to_db import connect_to_batabase
from psycopg2.extras import NamedTupleCursor
from datetime import datetime

conn = connect_to_batabase()


def get_information_by_card(card_id: int):

    child_id = []
    door_id = []
    door_id_card = []
    d_num = []
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(f'SELECT * FROM cards WHERE id={card_id}')
        cards = curs.fetchone()
        if cards==None:
           print("Карты с таким ID не существует, введите другое значение")
        else:
            people_id = cards.people_id
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(f'SELECT name, phone, role_id FROM peoples WHERE id={people_id}')
                people = curs.fetchone()
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(f'SELECT * FROM people_child WHERE id={people_id}')
                childs = curs.fetchall()
                for i in range(0, len(childs)):
                    child_id.append(str(childs[i][0]))
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(f"SELECT door_id FROM door_people WHERE people_id={people_id}")
                pd = curs.fetchall() #return [Record(door_id=N)]
                for i in range(0, len(pd)):
                    door_id.append(str(pd[i][0]))
                
                for id in door_id:
                    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                        curs.execute(f"SELECT * FROM doors WHERE id={id}")
                        door = curs.fetchall()
                        d_num.append(door[0].door_num)
                        door_id_card.append(door[0].id)
                #print(pd)
                # print(f"Информация о человеке \nимя: {str(peoples[0].name)}, \nномер телефона:{str(peoples[0].phone)}, \nID роли: {str(peoples[0].role_id)}")
                # print(f"Доступные человеку двери: {d_num}")

    #return door_id_card
    return {
        "Человек" : people,
        "Двери, которые может он может открыть": door_id,
        "Двери, к которым дан доступ": door_id_card,
        "Дети" : child_id
        }


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
    return door_id_reader

print("Введите ID карты")
dc = input()
print("Введите ID считывателя")
dr = input()

print(get_information_by_card(dc))

door_id_card = get_information_by_card(dc)["Двери, к которым дан доступ"]
door_id_reader = get_infornation_by_reader(dr)


def access(door_id_c, door_id_r):
    ob = []
    # print(door_id_c, len(door_id_c))
    # print(door_id_r, len(door_id_r))
    for i in door_id_c:
        for j in door_id_r:
            if i == j:
                ob.append(i)
    if len(ob)!=0:
        print(f"access is allowed")
    else:
        print(f"access denied")
        return "нет доступных для открытия дверей"
    return ob

#print("ID дверей: " + str(access(door_id_card, door_id_reader)))


