from tkinter import *
import time
import alert
import baza.db_fases as db
from PIL import ImageTk, Image
import cv2
import FaceAlgo
import CameraWindow


from win32api import GetSystemMetrics
print("Screen width =", GetSystemMetrics(0))
screen_width = GetSystemMetrics(0)
print("Screen height =", GetSystemMetrics(1))
screen_height = GetSystemMetrics(1)

window_height = 545
window_width = 700


#Capture video frames
bluure=5
mashtab=1
face_cascade = cv2.CascadeClassifier('C:\CV_Start\haarcascades\haarcascade_frontalface_default.xml')
count_frame=0
detect_faces_opencv=False

def show_frame():
    #print("получили кадр")
    global lmain, cap, var0, mashtab, count_frame, detect_faces_opencv, nameMTS

    _, frame = cap.read()
    count_frame+=1




    frame, face_descriptors = FaceAlgo.find_faces_in_image(frame, bluure, True )

    for face_descriptor in face_descriptors:
        #отрисовываем и проверяем все найденные лица
        ret, dist = FaceAlgo.compare_face(face_descriptor[0])
        print(ret, dist)

        # if ret:
        #     if len(ret)>0:
        #         d = face_descriptor[1]
        #         cv2.putText(frame, str(str(round(dist,2))+" "+str(ret[2])), (d.left(), d.top()), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255,0), 2)
        #         print ("Похож на ", ret[2])
        # else:
        #     print("Улыбочку!)")


    frame = cv2.resize(frame, None, fx=mashtab, fy=mashtab, interpolation=cv2.INTER_CUBIC)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    img = ImageTk.PhotoImage(image=img)

    # lmain.image = img
    lmain.imgtk = img
    lmain.configure(image=img)



    #lmain.image = img
    lmain.after(1, show_frame)

def save_bluur():
    global bluure, bluur_entry
    bluure=int(bluur_entry.get())


def set_mashtab_30():
    global  mashtab
    mashtab = 0.3

def set_mashtab_50():
    global  mashtab
    mashtab = 0.5

def set_mashtab_70():
    global  mashtab
    mashtab = 0.7

def set_mashtab_100():
    global  mashtab
    mashtab = 1

def WindowsCamera(data, flag_opencv=False):

    global lmain, cap, var0, bluur_entry, detect_faces_opencv
    detect_faces_opencv =flag_opencv
    t_c =  Toplevel()
    t_c.title(str("Захват изображения"))
    x = round((screen_width / 2) - (window_width / 2))
    y = round((screen_height / 2) - (window_height / 2))
    t_c.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    #t_c.geometry('670x530+200+200')  # ширина=500, высота=400, x=300, y=200
    #t.minsize(width=400, height=200)
    #t.resizable(True, True)  # размер окна может быть изменён только по горизонтали
    t_c.resizable(False, False)  # размер окна может быть изменён только по горизонтали
    t_c.lift()

    frame1 = Frame(t_c)
    frame1.grid(row=0, column=0)

    #cap = cv2.VideoCapture(0)
    cap = data

    _, frame = cap.read()


    lmain = Label(frame1)

    def cansel():
        t_c.destroy()
        time.sleep(1)
        CameraWindow.WindowsCamera(cap, False)

    def takeApicture():
        t_c.destroy()
        time.sleep(2)
        CameraWindow.WindowsCamera(cap, False)


    lmain.grid(row=0, column=0, sticky=(N, W, E, S))
    ch1 = Button(frame1, text="<< Отменить", width=13, command=cansel)
    ch1.grid(row=1, column=0, sticky=(N, W, E, S))
    ch2 = Button(frame1, text="Сделать фото", width=20, command = takeApicture)
    ch2.grid(row=1, column=0, sticky=(N, W, E, S))


    show_frame()  # Display 2

