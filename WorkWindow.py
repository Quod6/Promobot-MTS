from tkinter import *

import baza.db_fases as db

import FaceAlgo

#
# import numpy as np
# from keras.models import Sequential
# from keras.layers import Dense, Dropout
#


def make_all_person():
    print("Выбираем все лица из noname. И делаем разнос по персонам")
    #начинаем перебор всех лиц, по похожести, и сравниваем с уж созданными персонами
    res,noname =db.search_person("noname")
    print("распределяем все лица по персонам. если уникальное, то создаем новую персону")

    FaceAlgo.load_all_faces()
    #перебираем все лица в noname, если нет похожих людей, то создаем новых
    faces, data = db.search_faces(noname)

    #print((data[0]))
    new_face_counter=0
    print("всего лиц ", len(data))
    for i in range(0, len(data)):
        #print("сравниваем лицо", data[i])
        if len(data[i])!=128:
            print (i,data[i])
        #перезагружаем всю базу, будет очень медленно
        #FaceAlgo.load_all_faces()
        #print("сравниваем лицо",i)
        ret, dist = FaceAlgo.compare_face(data[i], 0.45, False)
        if ret:
                if len(ret)>0:
                    print(ret)
                    # оценка, имя персоны, id персоны, дескриптор
                    print ("Похож на ", ret[1], dist)
                    # находим персону в базе
                    #print(ret)

                    if dist>0.1:
                        res, pers = db.search_person_id(ret[1])
                        if res:
                            print("Добавляем лицо в персону", pers.name)
                            #db.set_face(pers, faces[i])
                            FaceAlgo.set_face(pers, faces[i])
                    # else:
                    #     print("Лицо не добавляем. сильно похожее")


        else:
            new_face_counter+=1
            facename = "name"+str(new_face_counter)

            new_p = db.add_person(facename)
            # добавляем неизвестно елицо в персну
            print("нет совпадений в лице создаем новую персону под лицо", facename, faces[i].id, faces[i].image_path )
            #db.set_face(new_p, faces[i])
            FaceAlgo.set_face(new_p, faces[i])


    #перезагружаем весь кэш. Поменялось многое
    FaceAlgo.load_all_faces()



def del_all_person(i):
    print("Удаляем все персоны, переносим все лица в noname...")
    db.reset_base()
    print("Удалили")

def compare_person(i):
    FaceAlgo.compare_face_by_id(23)
    FaceAlgo.compare_face_by_id(3)

def make_keras(i):

    #FaceAlgo.clear_noname()
    FaceAlgo.delEmptyFaces()
    # data  = FaceAlgo.load_all_faces()
    # #face.id, person.id, person.name, face.image_path, data_f
    # print(data[0])
    # x_train = np.random.random((len(data), 128))
    # y_train = np.random.random((len(data), 1))
    #
    # for i in range(0, len(data)):
    #     x_train[i] = np.asarray(data[i][4])
    #     y_train[i] = int(data[i][1])

    #y_train = np.random.random((len(data), 1))

    #print(x_train[0], y_train[0])
    # Generate dummy data
    # x_train = np.random.random((1000, 128))
    # y_train = np.random.randint(2, size=(1000, 1))
    # x_test = np.random.random((100, 128))
    # y_test = np.random.randint(2, size=(100, 1))
    # #
    # print(x_train[0], y_train[0])
    # print(len(x_train[0]), len(y_train[0]))
    #
    # model = Sequential()
    # model.add(Dense(512, activation='relu', input_dim=128))
    #
    # model.add(Dropout(0.2))
    # model.add(Dense(max(y_train), activation='softmax'))

    # model.compile(loss='categorical_crossentropy',
    #               optimizer='adam',
    #               metrics=['accuracy'])

    # model = Sequential()
    # model.add(Dense(64, input_dim=128, activation='relu'))
    # model.add(Dropout(0.5))
    # model.add(Dense(64, activation='relu'))
    # model.add(Dropout(0.5))
    # model.add(Dense(1, activation='sigmoid'))
    #
    # model.compile(loss='binary_crossentropy',
    #               optimizer='rmsprop',
    #               metrics=['accuracy'])
    #
    # model.fit(x_train, y_train,
    #           epochs=20,
    #           batch_size=16)
    # score = model.evaluate(x_test, y_test, batch_size=128)
    return
def del_buff(i):
    answer, person_buf = db.search_person("bufer")
    if answer:
        for f in person_buf.face:
            db.del_face(f)

    FaceAlgo.clear_noname()

def WindowsWork():
    global lmain, cap
    t_w =  Toplevel()
    t_w.title(str("Работа с данными"))
    t_w.geometry('600x400+200+200')  # ширина=500, высота=400, x=300, y=200
    #t.minsize(width=400, height=200)
    #t.resizable(True, True)  # размер окна может быть изменён только по горизонтали
    t_w.resizable(False, False)  # размер окна может быть изменён только по горизонтали


    #lmain = Label(frame1).grid(row=0, column=0, sticky=(N, W, E, S))
    #lmain = Button(frame1)

    #lmain.grid(row=0, column=0, sticky=(N, W, E, S))


    # panel = Label(t, image=image)
    # lmain = frame1.Label(image)
    # lmain.grid(row=0, column=0)
    #

    but_save = Button(t_w, text="Разнести лица по персонам", command=lambda i=-1: make_all_person(i)).grid(row=0, column=0, sticky=(W))
    but_del_all = Button(t_w, text="Удалить все персоны", command=lambda i=-1: del_all_person(i)).grid(row=0,column=1, sticky=(W))
    but_compare = Button(t_w, text="Сравнить лицо", command=lambda i=-1: compare_person(i)).grid(row=0, column=2,
                                                                                                       sticky=(W))
    but_compare = Button(t_w, text="Удалить пустые персоны", command=lambda i=-1: make_keras(i)).grid(row=1, column=1,
                                                                                                       sticky=(W,E))





    # #frame1.pack()
    # e_name = Entry(frame1)
    #
    # e_second_name = Entry(frame1)
    # l_name = Label(frame1, text="Имя")
    # l_secon_name = Label(frame1, text="Фамилия")
    #
    # but_save = Button(frame1, text="Сохранить")
    #
    # e_name.grid(row=0, column=1, padx=20)
    # e_second_name.grid(row=1, column=1, padx=20)
    # l_name.grid(row=0, column=0, padx=20)
    # l_secon_name.grid(row=1, column=0, padx=20)
    # but_save.grid(row=0, column=2, padx=20)
    #
    # #нижний фрэйм на нем будем размещать список лиц и фотки
    # frame2 = Frame(t,width = 500, height=400)
    # frame2.grid(row=1, column=0)
    #
    # frame3 = Frame(frame2)
    # frame3.grid(row=0, column=0)
    # frame4 = Frame(frame2, bg = "gray")
    # frame4.grid(row=0, column=1, sticky=N)
    #
    # listbox_faces = Listbox(frame3, bg='white', height=33)
    # listbox_faces.config(selectmode=MULTIPLE)

    # but_step1 = Button(frame3, text= '<<', command=lambda i=-1: page_change(i)).grid(row=5, column=0, sticky=(N, W, E, S))
    # but_step2 = Button(frame3, text='>>', command=lambda i=1: page_change(i)).grid(row=6, column=0, sticky=(N, W, E, S))
    # but_cut = Button(frame3, text= 'Вырезать', command=lambda i=person: onCut(i)).grid(row=2, column=0, sticky=(N, W, E, S))
    # but_paste = Button(frame3, text='Вставить', command=lambda i=person: onPaste(i)).grid(row=1, column=0, sticky=(N, W, E, S))
    # but_del = Button(frame3, text='Удалить', command=lambda i=person: onDel(i)).grid(row=3, column=0, sticky=(N, W, E, S))

    #WindowfPersonRefresh(person)

