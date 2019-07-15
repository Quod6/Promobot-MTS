from tkinter import *
import baza.db_fases as db
from PIL import ImageTk, Image
from datetime import date
import time
import cv2
import FaceAlgo

person_list1=-1
person_list1=-1
persons2=[]



def OnSelect1(event):
    global all_person, person_list1, persons2, frame3, frame2
    #print("click")
    # selections = listbox.curselection()  # tuple of digit-string(s), aTupleOfSTRINGs, where digit-string(s) range from { 0, 1, .., N-1 }
    # selections = [int(x) + 1 for x in selections]  # transform string(s) to shifted int(s), make 'em { 1, 2, .., N }
    if listbox1.curselection():
        person_list1 = all_person[listbox1.curselection()[0]]
        print("выделили", person_list1.name)
        list_comp = FaceAlgo.ComparePersons(all_person[listbox1.curselection()[0]])

        listbox2.delete(0, END)

        persons2.clear()
        # добавляем в лист бокс данные
        for p in list_comp:
            # listbox.insert(END, str(p.name+" "+p.second_name) )
            listbox2.insert(END, str(str(p[2])+ " "+str(round(p[5],2))) )
            ret, p  = db.search_person_id(p[1])
            if ret:
                persons2.append(p)
        listbox2.grid(row=0, column=4, padx=10, pady=10)

        list = frame2.grid_slaves()
        for l in list:
            l.destroy()

        list = frame3.grid_slaves()
        for l in list:
            l.destroy()




        row_c=0
        count=0
        for face in person_list1.face:
            count+=1
            if count>3:
                break
            frame = cv2.imread(face.image_path)
            height, width = frame.shape[:-1]
            if height > 0 and width > 0:
                frame = cv2.resize(frame, (115, 115), interpolation=cv2.INTER_CUBIC)
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                # imgtk = ImageTk.PhotoImage(image=img)

                # img = ImageTk.PhotoImage(Image.open(face.image_path))
                img = ImageTk.PhotoImage(image=img)

                # print(face.image_path)
                # panel = Label(t, image=img)

                # panel = Label(t, text = face.image_path)

                panel = Button(frame3, image=img)
                # panel = Button(t, image=img, text=c)
                # panel.bind('<Button-1>', push_image)

                panel.image = img
                panel.grid(row=row_c, column=0, sticky=(N, W, E, S))
                row_c += 1
def OnSelect2(event):
    global all_person, person_list2, persons2, listbox2, frame2
    #print("click")
    # selections = listbox.curselection()  # tuple of digit-string(s), aTupleOfSTRINGs, where digit-string(s) range from { 0, 1, .., N-1 }
    # selections = [int(x) + 1 for x in selections]  # transform string(s) to shifted int(s), make 'em { 1, 2, .., N }
    for p in persons2:
        print(p.name)

    if listbox2.curselection():

        person_list2 = persons2[listbox2.curselection()[0]]
        print("выделили2", person_list2.name)



    list = frame2.grid_slaves()
    for l in list:
        l.destroy()

    row_c=0
    count=0
    for face in person_list2.face:
        count+=1
        if count>3:
            break
        frame = cv2.imread(face.image_path)
        height, width = frame.shape[:-1]
        if height > 0 and width > 0:
            frame = cv2.resize(frame, (115, 115), interpolation=cv2.INTER_CUBIC)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            # imgtk = ImageTk.PhotoImage(image=img)

            # img = ImageTk.PhotoImage(Image.open(face.image_path))
            img = ImageTk.PhotoImage(image=img)

            # print(face.image_path)
            # panel = Label(t, image=img)

            # panel = Label(t, text = face.image_path)

            panel = Button(frame2, image=img)
            # panel = Button(t, image=img, text=c)
            # panel.bind('<Button-1>', push_image)

            panel.image = img
            panel.grid(row=row_c, column=0, sticky=(N, W, E, S))
            row_c += 1

def Merge(i):
    global person_list1, person_list2


    if person_list1==-1 or person_list2==-1:
        print("не выбраны персоны")
        return

    if i==-1:
        FaceAlgo.mergerPerson(person_list1,person_list2 )
    if i == 1:
        FaceAlgo.mergerPerson(person_list2, person_list1)
    return

def WindowsSort():
    global  person_in_window, listbox1, listbox2, frame1,  e_name, e_second_name, t, page_win_person, frame2, frame3, all_person

    page_win_person=0
    t =  Toplevel()
    t.title("Сортировка персон")
    t.geometry('1000x730+100+200')  # ширина=500, высота=400, x=300, y=200
    #t.minsize(width=400, height=200)
    #t.resizable(True, True)  # размер окна может быть изменён только по горизонтали
    t.resizable(False, False)  # размер окна может быть изменён только по горизонтали


    frame1 = Frame(t)
    frame1.grid(row=0, column=0)

    # #frame1.pack()
    # e_name = Entry(frame1)
    #
    # e_second_name = Entry(frame1)
    # l_name = Label(frame1, text="Имя")
    # l_secon_name = Label(frame1, text="Фамилия")
    #
    # but_save = Button(frame1, text="Сохранить", command=lambda i=person: save_person(i))
    # # Button.config(selectmode=SINGLE)  # see above EXTENDED
    # # Button.bind("<<ListboxSelect>>", save_person)
    #
    # e_name.grid(row=0, column=1, padx=20)
    # e_second_name.grid(row=1, column=1, padx=20)
    # l_name.grid(row=0, column=0, padx=20)
    # l_secon_name.grid(row=1, column=0, padx=20)
    # but_save.grid(row=0, column=2, padx=20)

    #нижний фрэйм на нем будем размещать список лиц и фотки
    frame2 = Frame(t)
    frame2.grid(row=0, column=5)
    frame3 = Frame(t)
    frame3.grid(row=0, column=1)

    #
    # frame3 = Frame(frame2)
    # frame3.grid(row=0, column=0)
    # frame4 = Frame(frame2, bg = "gray")
    # frame4.grid(row=0, column=1, sticky=N)
    #
    listbox1 = Listbox(frame1, bg='white', height=20)
    listbox1.config(selectmode=SINGLE)
    listbox1.bind("<<ListboxSelect>>", OnSelect1)

    listbox2 = Listbox(frame1, bg='white', height=20)
    listbox2.config(selectmode=SINGLE)
    listbox2.bind("<<ListboxSelect>>", OnSelect2)

    but_step1 = Button(frame1, text= '<<', command=lambda i=-1: Merge(i)).grid(row=0, column=2, sticky=(N, W, E, S))
    but_step2 = Button(frame1, text='>>', command=lambda i=1: Merge(i)).grid(row=0, column=3, sticky=(N, W, E, S))

    #
    # but_step1 = Button(frame3, text= '<<', command=lambda i=-1: page_change(i)).grid(row=5, column=0, sticky=(N, W, E, S))
    # but_step2 = Button(frame3, text='>>', command=lambda i=1: page_change(i)).grid(row=6, column=0, sticky=(N, W, E, S))
    # but_cut = Button(frame3, text= 'Вырезать', command=lambda i=person: onCut(i)).grid(row=2, column=0, sticky=(N, W, E, S))
    # but_paste = Button(frame3, text='Вставить', command=lambda i=person: onPaste(i)).grid(row=1, column=0, sticky=(N, W, E, S))
    # but_del = Button(frame3, text='Удалить', command=lambda i=person: onDel(i)).grid(row=3, column=0, sticky=(N, W, E, S))

    # загружаем лица с базы в файл кэша, если еще не загруженны
    #FaceAlgo.LookMassFaces()


    listbox1.delete(0,END)
    all_person = db.select_all_person()

    # добавляем в лист бокс данные
    for p in all_person:
        #listbox.insert(END, str(p.name+" "+p.second_name) )
        listbox1.insert(END, str(p.name))

    listbox1.grid(row=0, column=0,  padx=10, pady=10)