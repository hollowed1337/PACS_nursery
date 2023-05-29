import psycopg2
from psycopg2.extras import NamedTupleCursor
from datetime import datetime

#conn = psycopg2.connect('postgresql://${DB_USER}:${DB_PASSWD}localhost:5432/${DB_NAME}')

try:
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='qwe', host='localhost')
except:
    print('Can`t establish connection to database')


cursor = conn.cursor()

# people_id = input()
people_id = 2



def get_information_by_card(card_id: int):

    role_id = []
    door_id_card = []
    d_num = []
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(f'SELECT * FROM cards WHERE id={card_id}')
        cards = curs.fetchone()
        if cards==None:
           print("Карты с таким ID не существует, введите другое значение")
        else:
            people_id = cards.people_id
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs: #ненужно
                curs.execute(f'SELECT name, phone, role_id FROM peoples WHERE id={people_id}') #ненужно
                peoples = curs.fetchall() #ненужно
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute(f"SELECT door_id FROM door_people WHERE people_id={people_id}")
                pd = curs.fetchall()
                for i in range(0, len(pd)):
                    role_id.append(str(pd[i][0]))
                
                for id in role_id:
                    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                        curs.execute(f"SELECT * FROM doors WHERE id={id}")
                        door = curs.fetchall()
                        d_num.append(door[0].door_num)
                        door_id_card.append(door[0].id)
                
                # print(f"Информация о человеке \nимя: {str(peoples[0].name)}, \nномер телефона:{str(peoples[0].phone)}, \nID роли: {str(peoples[0].role_id)}")
                # print(f"Доступные человеку двери: {d_num}")

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
    return door_id_reader


dc = input()
dr = input()

door_id_card = get_information_by_card(dc)
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
print(access(door_id_card, door_id_reader))




def create_log(card_id: int, reader_id):

    date = datetime.now()        
    if len(card_id)==0 or len(reader_id)==0:
        print("Данные отсутствуют")
    else:
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute(f"INSERT INTO logs (id_reader, id_card, date) VALUES ('{reader_id}', '{card_id}', '{date}')"
                         )
        conn.commit()



create_log(dc, dr)
