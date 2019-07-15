from tkinter import *
import baza.db_fases as db
from PIL import ImageTk, Image
from datetime import date
import time
import cv2


max_in_page  = 35

def onCut(person):
    global listbox_faces,page_win_person, max_in_page
    #values = [listbox_faces.get(idx) for idx in listbox_faces.curselection()]

    answer, person_buf = db.search_person("bufer")
    if answer:

        # for face in person.face:
        #     print(face)
        list_faces = []
        for n in listbox_faces.curselection():
            #print()
            list_faces.append( person.face[int(page_win_person*max_in_page +n)])

            print(n)
        for f in list_faces:
            db.set_face(person_buf, f)

    WindowfPersonRefresh(person)

def onPaste(person):
    global listbox_faces
    # переносим из bufer в выбранный профиль
    answer, person_buf = db.search_person("bufer")
    if answer:
        for f in person_buf.face:
            db.set_face(person, f)
    WindowfPersonRefresh(person)

def onDel(person):
    global listbox_faces
    # переносим из bufer в выбранный профиль
    answer, person_buf = db.search_person("bufer")
    if answer:
        for f in person_buf.face:
            db.del_face(f)

    WindowfPersonRefresh(person)

def WindowfPersonRefresh(person):
    global frame4, e_name, e_second_name, t, page_win_person
    # обновляем данные на окне
    e_name.delete(0, END)

    e_name.insert(END, person.name)


    row_c=0
    col_c=0
    c=0
    listbox_faces.delete(0,END)

    list = frame4.grid_slaves()
    for l in list:
        l.destroy()

    count_faces=0
    for face in person.face:
        #print(page_win_person*max_in_page, page_win_person*max_in_page+max_in_page)
        if count_faces>=page_win_person*max_in_page and count_faces<page_win_person*max_in_page+max_in_page:
            try:
                listbox_faces.insert(END, face)
                frame = cv2.imread(face.image_path)
                height, width = frame.shape[:-1]
                if height>0 and width>0:
                    frame = cv2.resize(frame, (115, 115), interpolation=cv2.INTER_CUBIC)
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                    img = Image.fromarray(cv2image)
                    #imgtk = ImageTk.PhotoImage(image=img)

                    #img = ImageTk.PhotoImage(Image.open(face.image_path))
                    img = ImageTk.PhotoImage(image=img)

                    #print(face.image_path)
                    #panel = Label(t, image=img)

                    #panel = Label(t, text = face.image_path)

                    panel = Button(frame4, image=img, command=lambda i=c: onClick(i))
                    #panel = Button(t, image=img, text=c)
                    #panel.bind('<Button-1>', push_image)

                    panel.image = img
                    panel.grid(row=row_c, column=col_c, sticky=(N, W, E, S))
                    col_c+=1
                    if col_c>6:
                        col_c=0
                        row_c+=1
                    c+=1
            except:
                print("ошибка вывода картинки", face.image_path )
                db.del_face(face)
        count_faces+=1

    listbox_faces.grid(row=0, column=0,  padx=10, pady=10)
    return
def page_change(index):
    global person_in_window,page_win_person, max_in_page
    page_win_person+=int(index)
    if page_win_person<0:
        page_win_person=0
    if page_win_person>=len(person_in_window.face)/max_in_page:
        page_win_person = int(len(person_in_window.face)/max_in_page)

    print(page_win_person)


    WindowfPersonRefresh(person_in_window)

def save_person(persone):
    global e_name, e_second_name
    print ("save", e_name.get(), e_second_name.get())
    persone.name = e_name.get()
    persone.second_name = e_second_name.get()

    persone.save()
    #persone.get(name=e_name.get(), second_name=e_second_name.get(), birthday=date(2007, 1, 10), is_relative=True)

    return

def onClick(index):
        global listbox_faces, page_win_person
        page_win_person = 0
        print("This is Button: " + str(index))
        #values = [listbox_faces.get(idx) for idx in listbox_faces.curselection()]

        flag= 0
        for i in listbox_faces.curselection():
            if i == index:
                flag=1

        if flag==1:
            print ("clear")
            listbox_faces.selection_clear(index, END)
        else:
            listbox_faces.selection_set(index)

        return


def WindowsPerson(person):
        global  person_in_window, listbox_faces, frame4,  e_name, e_second_name, t, page_win_person, present, panel, frame6
        person_in_window = person
        page_win_person=0
        t =  Toplevel()
        t.title(str(person.name )+ " " + str(person.second_name ))
        t.geometry('1000x730+200+100')  # ширина=500, высота=400, x=300, y=200
        #t.minsize(width=400, height=200)
        #t.resizable(True, True)  # размер окна может быть изменён только по горизонтали
        t.resizable(False, False)  # размер окна может быть изменён только по горизонтали


        frame1 = Frame(t)
        frame1.grid(row=0, column=0)

        #frame1.pack()
        e_name = Entry(frame1)

        l_name = Label(frame1, text="Имя")

        but_save = Button(frame1, text="Сохранить", command=lambda i=person: save_person(i))
        # Button.config(selectmode=SINGLE)  # see above EXTENDED
        # Button.bind("<<ListboxSelect>>", save_person)

        e_name.grid(row=0, column=1, padx=20)
        l_name.grid(row=0, column=0, padx=20)
        but_save.grid(row=0, column=2, padx=20)




        #нижний фрэйм на нем будем размещать список лиц и фотки
        frame2 = Frame(t,width = 500, height=400)
        frame2.grid(row=1, column=0)

        frame3 = Frame(frame2)
        frame3.grid(row=0, column=0)

        frame4 = Frame(frame2, bg = "gray")
        frame4.grid(row=0, column=1, sticky=N)


        listbox_faces = Listbox(frame3, bg='white', height=33)
        listbox_faces.config(selectmode=MULTIPLE)

        but_step1 = Button(frame3, text= '<<', command=lambda i=-1: page_change(i)).grid(row=5, column=0, sticky=(N, W, E, S))
        but_step2 = Button(frame3, text='>>', command=lambda i=1: page_change(i)).grid(row=6, column=0, sticky=(N, W, E, S))
        but_cut = Button(frame3, text= 'Вырезать', command=lambda i=person: onCut(i)).grid(row=2, column=0, sticky=(N, W, E, S))
        but_paste = Button(frame3, text='Вставить', command=lambda i=person: onPaste(i)).grid(row=1, column=0, sticky=(N, W, E, S))
        # but_del = Button(frame3, text='Удалить', command=lambda i=person: onDel(i)).grid(row=3, column=0, sticky=(N, W, E, S))


        WindowfPersonRefresh(person)


