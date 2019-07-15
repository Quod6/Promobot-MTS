from peewee import *
from datetime import date
import time
import os
#import FaceAlgo

db = SqliteDatabase('baza/people.db')


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


class Person(Model):
    name = CharField()
    second_name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db


class Face(Model):
    owner = ForeignKeyField(Person, related_name='face')
    image_path = CharField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'


class Data(Model):
    owner = ForeignKeyField(Face, related_name='data')
    code = CharField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'


def create_tables():
    # Создание таблиц в базе
    try:
        Person.create_table()
        print("создали Person")
        Person.create(name='noname', second_name='для сбора всех подряд фотографий', birthday=date(2007, 1, 10), is_relative=True)
        Person.create(name='bufer', second_name='Для обмена фотографиями', birthday=date(2007, 1, 10), is_relative=True)
    except:
        print("таблица Person уже создана")

    try:
        Face.create_table()
        print("создали Face")
    except:
        print("таблица Face уже создана")

    try:
        Data.create_table()
        print("создали Data")
    except:
        print("таблица Data уже создана")




def add_person(name="test", second_name="", birthday=date(2018, 1, 10)):
    # добавляем  в базу  нового человека
    person = Person.create(name=name, second_name=second_name, birthday=birthday, is_relative=True)
    print("добавили в базу: ", name, second_name, birthday)
    return person


def search_person(name):
    # поиск человека в базе
    try:
        #print("поиск", name)
        person = Person.get(Person.name == name)
        #print("найден человек:", person.name, person.id)
        return True, person
    except:
        print("Ничего не найдено")
        return False, 0

def search_person_id(id):
    # поиск человека в базе
    try:
        #print("поиск по id", id)
        person = Person.get(Person.id == id)
        #print("найден человек:", person.name, person.id)
        return True, person
    except:
        print("Ничего не найдено")
        return False, 0

def add_face(person, face_file, face_descriptor):
    # добавляем персоне новое лицо и метрику по нему
    image_p = face_file  # 'c:/faces/1.jpg'
    #with Profiler() as p:
    face = Face.create(owner=person, image_path=image_p)
    #print("добавляем новое лицо персоне")

    # face_descriptor = [0.3,0.7,-0.9]
    lists = [{'owner': face, 'code': x} for x in face_descriptor]
    # print(lists)
    with Profiler() as p:
        Data.insert_many(lists).execute()
        # for code in face_descriptor:
        # Data.create(owner=face, code=code)
    return face


def search_faces(person):
    # ищем все лица персоны
    faces = []
    data = []
    try:
        for p in person.face:
            # print(p.image_path)
            faces.append(p)
            data_f = []
            # перебираем все признаки в лице, создаем отдельный лист с ними
            for d in p.data:
                data_f.append(float(d.code))

            data.append(data_f)
            # print(data_f)

        return faces, data
    except:
        print("ошибка поиска лиц в персоне")
        return faces, data

# create_tables()
def select_all_person():
    persons =[]
    for person in Person.select():
        persons.append(person)
    return persons

def set_face( person, face):
    #Назначаем лицо персоне
    print("перенос лица", person.name, face.image_path)

    face.owner = person.id
    face.save()

def del_face(face):
    # уничтожаем с базы данных все записи, и файл с директории
    # list_del=[]
    # for data in face.data:
    #     #print(data.code)
    #     list_del.append(data)
    #
    # for d in list_del:
    #     d.delete()
    #
    with Profiler() as p:
        Data.delete().where(Data.owner == face).execute()

        #print("удаляем файл", face.image_path)
        try:
            os.remove(face.image_path)
        except:
            print ("нету скриншота")
        face.delete_instance()

def change_persone(persone, name, second_name, birthday):
    # изменяем персону
    persone.name = name
    persone.second_name = second_name
    persone.birthday = birthday
    persone.save()

    #person_new = Person.get(Person.get_id == )
    return

def del_persone(persone):
    print("удаляем персону ", persone.name)

    for f in persone.face:
        del_face(f)
    persone.delete_instance()

def del_face_in_persone(persone):

    print("удаляем все лица с персоны ", persone.name)

    for f in persone.face:
        del_face(f)
    persone.save()

def reset_base():
    # все лица переносим в noname и уничтожаем всех персон

    all = select_all_person()
    print("выбираем всех персон ", len(all))
    res,noname =search_person("noname")
    print(noname.name, noname.id)

    print("перебираем их всех")
    for p in all:
        if p.name!="noname" and p.name!="bufer":
            # переписываем все лица на нонэйм и удаляем персону
            for f in p.face:
                f.owner = noname.id
                f.save()
            p.delete_instance()

    return



