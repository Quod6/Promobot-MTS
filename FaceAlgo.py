from tkinter import *
from PIL import ImageTk, Image
import baza.db_fases as db
from scipy.spatial import distance
import dlib
import alert



import numpy as np
import cv2

import time

import baza.db_fases as db

mass_faces =[]

face_cascade = cv2.CascadeClassifier('C:\CV_Start\haarcascades\haarcascade_frontalface_default.xml')
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

def del_buff():
    print("Чистим буфер")
    answer, person_buf = db.search_person("bufer")
    if answer:
        for f in person_buf.face:
            db.del_face(f)

def clear_noname():
    #удаляем все лица c noname
    res, noname = db.search_person("noname")
    db.del_face_in_persone(noname)

AddQ = True
ii = 0

def name(name, per):
    global nameMTS, personMTS
    nameMTS = name
    personMTS = per

def find_faces_in_image( image, bluur, nameMTS="noname", add_flag=False):
    global personMTS, AddQ
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bluur_image = int(cv2.Laplacian(gray, cv2.CV_64F).var())
    #cv2.imshow("Video", image)
    #print("bluure", bluur_image)

    if bluur_image < bluur:
        #print("bad bluure", bluur)
        cv2.putText(image, str(bluur_image), (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        return image, []

    cv2.putText(image, str(bluur_image), (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


    img = image
    img_show = image.copy()
    #img2 = image
    # img2 = cv2.resize(image, None, fx=0.50, fy=0.5, interpolation=cv2.INTER_CUBIC)

    dets_webcam = detector(img, 1)
    face_descriptors = []
    #face_descriptor=[]

    for k, d in enumerate(dets_webcam):

        face = img[d.top(): d.bottom(), d.left():d.right()].copy()
        if d.left() < 0 or d.top() < 0:
            print("плохие границы под лицо")
            continue

        if abs(d.left() - d.right()) < 150:
            print("маленькое лицо. отбраковываем", d.left() - d.right())
            continue

        #cv2.rectangle(img_show, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
        #cv2.imshow("Video", img_show)
        #cv2.waitKey(1)
        #print(d.bottom(), d.top(), d.right(), d.left())
        # cv2.imshow("Face", face)

        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)

        #cv2.putText(img, ret[2], (l, t), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        #
        # # print(face_descriptor)
        #
        if add_flag:
            answer, person = db.search_person(nameMTS)

            if answer:
                print(person.name)
                # добавим новое лицо найденному человеку

                #gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                #print(np.max(cv2.convertScaleAbs(cv2.Laplacian(gray, 3))))

                # производим поиск и в noname тоже
                ret, dist = compare_face(face_descriptor, 0.5, True)
                #print("схожесть", dist, ret)

                #if ret:
                    #    if len(ret)>0:
                if len(face_descriptor) > 0:
                        if dist>0.3:
                            print("Добавляем лицо в базу")
                            face_file = 'c:/faces_db1/' + str(int(time.time())) + '.jpg'
                            # face =cv2.resize(face, (100, 100), interpolation=cv2.INTER_CUBIC)
                            cv2.imwrite(face_file, face)
                            # face_descriptor = [0.3, 0.7, -0.9]


                            add_face(personMTS, face_file, face_descriptor)
                            #face = db.add_face(person, face_file, face_descriptor)

                        else:
                            print("В базе есть сильно похожее лицо, не добавляем")

        face_descriptors.append([face_descriptor, d])
        #return img_show, face_descriptor, d
    return img_show, face_descriptors

def load_all_faces():
    global mass_faces, noname
    print("Загружаем данные с базы...")
    mass_faces.clear()
    all = db.select_all_person()
    res,noname =db.search_person("noname")
    for person in all:
        #if person.name != "noname" and person.name != "bufer":
            for face in person.face:
                #print(face.image_path)
                #faces.append(p.image_path)
                data_f = []
                for d in face.data:
                    data_f.append(float(d.code))
#                print (len(data_f))
                mass_faces.append([face.id, person.id, person.name, face.image_path, data_f ])
    print("Загрузили")
    return mass_faces
    # распечатываем подготовленный массив
    # for m in mass_faces:
    #     print (m)

def compare_face(face_descriptor, porog=0.5, no_noname=False, my_id=-1):
    global mass_faces, noname
    if len(mass_faces)==0:
        load_all_faces()

    if len(face_descriptor)!=128:
        print ("неверный дискриптор!")
        return []
    result = []

    # перебираем все лица, и создаем массив похожестей
    for data in mass_faces:
        # с собой не сравниваем
        #надо добавить чтобы не смотрели noname
        if data[0] != face_descriptor:
            if no_noname==False:
                if data[1]==noname.id:
                    #print("не смотрим в noname")
                    continue
            if my_id>=0:
                if my_id==data[1]:

                    continue
            #print("Сравниваем", data[3])
            #print(face_descriptor)
            #print(data[4])
            dist = distance.euclidean(face_descriptor, data[4])
            #dist = distance.euclidean(face_descriptor[0:3], data[4][0:3])

            # print("отличие", dist, data[2], data[1], data[4])
            #  в массив с результатами заносим только совпадения которые ниже порога
            if dist < porog:
                # оценка, имя персоны, id персоны, дескриптор
                result.append([dist, data[2], data[1], data[4]])

    # сортируем массив по уровню попадания
    result = sorted(result, key=lambda x: x[0])
    #print(result)
    #for r in result:
    #      print (r)

    if len(result)>0:
        mass_id = []
        for r in result:
            mass_id.append(r[2])
        #print(mass_id)

        max_face = np.median(mass_id)

        #print("схожесть c id", max_face)

        for d in mass_faces:
            if d[1]== max_face:
                #print("возвращаяе", d)
                #[face.id, person.id, person.name, face.image_path, data_f ]

                return d, result[0][0]

    return [], 1



def compare_face_by_id(id, porog=0.5):
    #сравниваем id лица  со всеми остальными, и выдаем результат а кого похоже
    # если массив не подготовлен. то разносим его
    global mass_faces, noname
    if len(mass_faces)==0:
        load_all_faces()

    #находим наше лицо, и берем его дескриптор
    face_descriptor=[]
    for data in mass_faces:
        if data[0]==id:
            face_descriptor=data.copy()
    # вызываем вункцию распознования лица по дискриптору
    print ("нашли дескриптор по id",face_descriptor)
    compare_face(face_descriptor[4], porog)


def set_face(persone, face):
    global mass_faces
    # меняем в кэше
    #print (result)
    for i in range(0, len(mass_faces)):
        if mass_faces[i][0]==face.id:
            mass_faces[i][1] = persone.id
    #меняем в базе
    db.set_face(persone, face)

def add_face(person, face_file, face_descriptor):
    global mass_faces
    # меняем в кэше
    #print (result)
    face = db.add_face(person, face_file, face_descriptor)
    data_f = []
    for d in face.data:
        data_f.append(float(d.code))
    #добавляем в кэш новое лицо
    mass_faces.append([face.id, person.id, person.name, face.image_path, data_f])

def LookMassFaces():
    # проверяем, загруженны ли все лица с базы
    global mass_faces, noname
    if len(mass_faces)==0:
        #если нет, то загружаем их в список
        load_all_faces()

def ComparePersons(person):

    #функция для сортировки персон
    #берем персону, и находим максимально похожии на нее персоны.
    print (person.name)
    if len(person.face)==0:
        print("пустая персона")
        return []
    #Ищем самую похожую персону
    list_max_comp=[]
    for face in person.face:
        # print(face.image_path)
        # faces.append(p.image_path)
        data_f = []

        for d in face.data:
            data_f.append(float(d.code))
            #                print (len(data_f))
        ret, dist = compare_face(data_f, 0.5, False, person.id)
        if len(ret)>0:
                flag_add=True
                # проверяем, есть ли уже в списке такая персона
                for t in list_max_comp:
                    if t[1]==ret[1]:
                        flag_add=False
                        break
                if flag_add:
                    ret.append(dist)
                    list_max_comp.append(ret)

    print("list")

    for t in list_max_comp:
        print(t)

    return list_max_comp

def mergerPerson(persone1, persone2):
    #забираем все лица из персоны 2 в персону 1.

    print("перенос лиц из ", persone2.name , " в персону:", persone1.name)
    for f in persone2.face:
        set_face(persone1, f)


def delEmptyFaces():
    print("Загружаем данные с базы...")
    mass_faces.clear()
    all = db.select_all_person()
    res, noname = db.search_person("noname")
    for person in all:
        if person.name!="noname" and person.name!="bufer":
            if len(person.face)==0:
                print("удаляем пустую персону", person.name)
                db.del_persone(person)







