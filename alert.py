from tkinter import *
from tkinter import ttk
import baza.db_fases as db
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import cv2
import PersonWindows
import CameraWindow
import CameraWindow2
import WorkWindow as ww
import SortWindow
import FaceAlgo
import  time
from tkinter import messagebox
import random

from win32api import GetSystemMetrics
print("Screen width =", GetSystemMetrics(0))
screen_width = GetSystemMetrics(0)
print("Screen height =", GetSystemMetrics(1))
screen_height = GetSystemMetrics(1)

window_height = 120
window_width = 270


bluure=5
mashtab=0.5
face_cascade = cv2.CascadeClassifier('C:\CV_Start\haarcascades\haarcascade_frontalface_default.xml')
count_frame=0



def CNP(cap):
    global nameMTS, feet
    reg = Tk()
    reg.title("Регистрация")
    x = round((screen_width / 2) - (window_width / 2))
    y = round((screen_height / 2) - (window_height / 2))
    reg.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    #reg.geometry('270x120+200+200')
    reg.lift()

    mainframe = ttk.Frame(reg, padding="15 15 15 15")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    mainframe2 = ttk.Frame(reg, padding="15 15 15 15")
    mainframe2.grid(column=0, row=1, sticky=(N, W, E, S))
    mainframe2.columnconfigure(0, weight=1)
    mainframe2.rowconfigure(0, weight=1)


    Label(mainframe, text="Создать новый профиль?", font='Arial 14').grid(column=25, row=2, sticky=N)

    def yes():
        global nameMTS, feet
        reg.destroy()

        regreg = Tk()
        regreg.title("Регистрация")
        x = round((screen_width / 2) - (window_width / 2))
        y = round((screen_height / 2) - (window_height / 2))
        regreg.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
        #regreg.geometry('263x120+200+200')

        mainframe2 = ttk.Frame(regreg, padding="15 15 15 15")
        mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe2.columnconfigure(0, weight=1)
        mainframe2.rowconfigure(0, weight=1)

        mainframe3 = ttk.Frame(regreg, padding="5 5 5 5")
        mainframe3.grid(column=0, row=1, sticky=(N, W, E, S))
        mainframe3.columnconfigure(0, weight=1)
        mainframe3.rowconfigure(0, weight=1)

        # Label(mainframe, text="Ваше фото", font='Arial 14').grid(column=0, row=0, sticky=N)
        #
        #
        #
        #
        # frame1 = Frame(mainframe)
        # frame1.grid(row=4, column=0)
        #
        # _, frame = cap.read()


        #
        # lmain = Label(frame1)
        #
        # lmain.grid(row=0, column=0, sticky=(N, W, E, S))
        #
        # frame, face_descriptors = FaceAlgo.find_faces_in_image(frame, bluure, True)
        #
        # for face_descriptor in face_descriptors:
        #     # отрисовываем и проверяем все найденные лица
        #     ret, dist = FaceAlgo.compare_face(face_descriptor[0])
        #     print(ret, dist)
        #     if ret:
        #         if len(ret) > 0:
        #             d = face_descriptor[1]
        #             cv2.putText(frame, str(str(round(dist, 2)) + " " + str(ret[2])), (d.left(), d.top()),
        #                         cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #             print("Похож на ", ret[2])
        #     else:
        #         print("no face")
        #
        # frame = cv2.resize(frame, None, fx=mashtab, fy=mashtab, interpolation=cv2.INTER_CUBIC)
        # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        # img = Image.fromarray(cv2image)
        # img = ImageTk.PhotoImage(image=img)
        #
        # # lmain.image = img
        # lmain.imgtk = img
        # lmain.configure(image=img)
        # #
        # # time.sleep(0.001)



        # Button(mainframe, text="Сделать снимок", width=15, command=yes).grid(column=5, row=25, sticky=(S, W))


        # def calculate(*args):
        #     print(feet.get())

        Label(mainframe2, text="Ваше имя", font='Arial 14').grid(column=0, row=0, sticky=N)
        # feet = StringVar()
        # feet_entry = ttk.Entry(regreg, width=7, textvariable=feet)
        # feet_entry.grid(column=2, row=1, sticky=(W, E))
        # ttk.Button(mainframe2, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
        feet = StringVar()
        feet_entry = ttk.Entry(mainframe2, width=10, textvariable=feet)
        feet_entry.grid(column=0, row=1, sticky=(W, E))
        nameMTS = feet.get()


        def cansel():
            regreg.destroy()
            time.sleep(1)
            CameraWindow.WindowsCamera(cap, False)

        def scan():
            global AddQ, personMTS, nameMTS, feet
            nameMTS = feet.get()#str(random.randint(1, 100))
            print("********")
            print("n " + nameMTS)

            db.add_person(nameMTS)
            answer, personMTS = db.search_person(nameMTS)
            FaceAlgo.name(nameMTS, personMTS)

            CameraWindow2.WindowsCamera(cap, True)
            regreg.destroy()


        Button(mainframe3, text="<< Отменить", width=13, command=cansel).grid(column=0, row=2, sticky=(S, E))
        Button(mainframe3, text="Продолжить >>", width=20, command=scan).grid(column=15, row=2, sticky=(S, E))

    def cansel():
        reg.destroy()
        time.sleep(1)
        CameraWindow.WindowsCamera(cap, False)


    Button(mainframe2, text="Да", width=10, command = yes).grid(column=0, row=15, sticky=(S, W))
    Button(mainframe2, text="Нет", width=10, command = cansel).grid(column=1, row=15, sticky=(S, E))


