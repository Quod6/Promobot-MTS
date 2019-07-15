from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from app import app
from app import mail
from app import s
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

import cv2
import matplotlib.pyplot as plt
import random
import jinja2
from jinja2 import Environment, FileSystemLoader, FunctionLoader
import time
import smtpd
import base64
import re
from werkzeug.utils import secure_filename


#-----------------------------------------
#face_recognition
from tkinter import *
import time
import alert
import baza.db_fases as db
from PIL import ImageTk, Image
import cv2
import FaceAlgo

import baza.db_fases as db
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import cv2
import PersonWindows
import CameraWindow
import WorkWindow as ww
import SortWindow
import FaceAlgo
import alert
import test
#-----------------------------------------


app.jinja_env.add_extension('jinja2.ext.loopcontrols')

#-----------------------------------------


# -----------------------------------------
# Загрузим все необходимые модули
import os
# Import smtplib for the sending function
import smtplib
# Import the email modules
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


import threading
from queue import Queue



f = open('userstatus.txt', 'w')

f.write('True\n')

f.close()

f = open('userstatus.txt')

userstatus = f.readline()
userstatus = userstatus[:-1]
print(userstatus)

f.close()

f = open('adminconfig.txt')

WIFI_login = f.readline()
print(WIFI_login)
WIFI_login = WIFI_login[:-1]

WIFI_password = f.readline()
print(WIFI_password)
WIFI_password = WIFI_password[:-1]

f.close()

f = open('map.txt')

floor_number = f.readline()[:-1]

floor_1_status = f.readline()
floor_1_status = floor_1_status[:-1]

floor_2_status = f.readline()
floor_2_status = floor_2_status[:-1]

floor_3_status = f.readline()
floor_3_status = floor_3_status[:-1]

floor_4_status = f.readline()
floor_4_status = floor_4_status[:-1]

floor_5_status = f.readline()
floor_5_status = floor_5_status[:-1]

floor_6_status = f.readline()
floor_6_status = floor_6_status[:-1]

floor_7_status = f.readline()
floor_7_status = floor_7_status[:-1]

floor_8_status = f.readline()
floor_8_status = floor_8_status[:-1]

floor_9_status = f.readline()
floor_9_status = floor_9_status[:-1]

floor_1_name = f.readline()[:-1]
floor_2_name = f.readline()[:-1]
floor_3_name = f.readline()[:-1]
floor_4_name = f.readline()[:-1]
floor_5_name = f.readline()[:-1]
floor_6_name = f.readline()[:-1]
floor_7_name = f.readline()[:-1]
floor_8_name = f.readline()[:-1]
floor_9_name = f.readline()[:-1]

f.close()

floor_1_status_ = "block"
floor_2_status_ = "block"
floor_3_status_ = "block"
floor_4_status_ = "block"
floor_5_status_ = "block"
floor_6_status_ = "block"
floor_7_status_ = "block"
floor_8_status_ = "block"
floor_9_status_ = "block"



# -----------------------------------------
# С какого адреса на какой будем посылать
# Также необходимо вписать свой пароль
me = 'promobot.mts@gmail.com'  # 'leksus.fm@gmail.com'
you = me  # 'lyosha.prim@mail.ru'
gmail_user = me
gmail_pwd = 'iKYO41EB'  # '1Adminsaitalyoshinru'
previous_page = ""

# ВНИМАНИЕ, чтобы скрипт работал, нужно
# разрешить непроверенные приложения
# https://www.google.com/settings/security/lesssecureapps
# ---------------------------------------
# Ошибки

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template(lang + '/404.html'), 404

# --------------------------------------

# ---------------------------------------
# Функции


def f_1():
    global istate
    # --------------------------------------
    # Языки

    lang = "ru"

    @app.route('/ru')
    def index_ru():
        global lang, previous_page
        lang = "ru"
        previous_page = "ru"
        return render_template("ru/index.html", WIFI_login=WIFI_login, WIFI_password=WIFI_password)

    @app.route('/en')
    def index_en():
        global lang, previous_page
        lang = "en"
        previous_page = "en"
        return render_template("en/index.html", WIFI_login=WIFI_login, WIFI_password=WIFI_password)

    @app.route('/ch')
    def index_ch():
        global lang, previous_page
        lang = "ch"
        previous_page = "ch"
        return render_template("ch/index.html", WIFI_login=WIFI_login, WIFI_password=WIFI_password)

    # --------------------------------------

    @app.route('/', methods=['GET', 'POST'])
    def index():
        person = "staff_CNP_staff"
        return render_template(lang + "/index.html", WIFI_login=WIFI_login, WIFI_password=WIFI_password, person_status=person)


    @app.route('/cnp', methods=['GET', 'POST'])
    def cnp():
        global nameMTS, statusMTS, Rtime, Btime
        if request.method == 'POST':
            nameMTS = request.form['nameMTS']
            print('name->> ', nameMTS)
            statusMTS = request.form['status']
            print('status->> ', statusMTS)
            if statusMTS == "Er":
                Btime = int(time.time()) + 30
            Rtime = 0
            return render_template(lang + "/cnps.html", time=Rtime)
        return render_template(lang + "/cnp.html")

    @app.route('/cnpfin', methods=['GET', 'POST'])
    def cnpfin():
        return render_template(lang + "/cnpfin.html")


    @app.route('/send-mail/')
    def send_mail():
        pass

    @app.route('/time')
    def time():
        global previous_page
        previous_page = "time"
        return render_template(lang + "/time.html")

    @app.route('/map')
    def map():
        global previous_page, floor_1_status, floor_2_status, floor_3_status, floor_4_status, floor_5_status, floor_6_status, floor_7_status, floor_8_status, floor_9_status, floor_1_status_, floor_2_status_, floor_3_status_, floor_4_status_, floor_5_status_, floor_6_status_, floor_7_status_, floor_8_status_, floor_9_status_
        previous_page = "map"
        if floor_1_status == "disabled":
            floor_1_status_ = "none"
        if floor_2_status == "disabled":
            floor_2_status_ = "none"
        if floor_3_status == "disabled":
            floor_3_status_ = "none"
        if floor_4_status == "disabled":
            floor_4_status_ = "none"
        if floor_5_status == "disabled":
            floor_5_status_ = "none"
        if floor_6_status == "disabled":
            floor_6_status_ = "none"
        if floor_7_status == "disabled":
            floor_7_status_ = "none"
        if floor_8_status == "disabled":
            floor_8_status_ = "none"
        if floor_9_status == "disabled":
            floor_9_status_ = "none"

        return render_template(lang + "/map.html", floor_a_status=floor_1_status_, floor_b_status=floor_2_status_,
                               floor_c_status=floor_3_status_, floor_d_status=floor_4_status_,
                               floor_e_status=floor_5_status_, floor_f_status=floor_6_status_,
                               floor_g_status=floor_7_status_, floor_h_status=floor_8_status_,
                               floor_i_status=floor_9_status_, floor_a_name=floor_1_name, floor_b_name=floor_2_name,
                               floor_c_name=floor_3_name, floor_d_name=floor_4_name, floor_e_name=floor_5_name,
                               floor_f_name=floor_6_name, floor_g_name=floor_7_name, floor_h_name=floor_8_name,
                               floor_i_name=floor_9_name)

    @app.route('/photo')
    def photo():
        global previous_page
        previous_page = "photo"
        return render_template(lang + "/photo.html")

    photo_index = 1

    @app.route('/email-send', methods=['GET', 'POST'])
    def email_send():
        global photo_index, you
        if request.method == 'POST':
            you = request.form['email_name'] + request.form['email']
            print(you)

            # -----------------------------------------
            # Создадим сообщение

            msg = MIMEMultipart()
            msg['Subject'] = 'Photo from MTS promobot :)'
            msg['From'] = me
            msg['To'] = you
            ImgFileName = "images/selfie (" + str(photo_index) + ").png"
            # добавлем к сообщению текст со ссылкой на вложенное изображение
            msgText = MIMEText('<b>Message text!</b><br><img src="cid:%s"><br>' % (ImgFileName), 'html')
            msg.attach(msgText)
            # считываем данные изображения
            img_data = open(ImgFileName, 'rb').read()
            # добавлем изображение
            image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
            image.add_header('Content-ID', '<{}>'.format(ImgFileName))
            msg.attach(image)
            # -----------------------------------------
            # Отправим наше письмо
            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            s.ehlo()
            s.login(gmail_user, gmail_pwd)
            s.sendmail(me, [you], msg.as_string())
            s.close()

            print(photo_index)
            photo_index += 1

            return render_template(lang + "/index.html", WIFI_login=WIFI_login, WIFI_password=WIFI_password)

        return render_template(lang + "/email-send.html")

    @app.route('/insta')
    def insta():
        global previous_page
        previous_page = "insta"
        return render_template(lang + "/insta.html")

    @app.route('/faq')
    def faq():
        global previous_page
        return render_template(lang + "/faq.html", previous_page=previous_page)

    @app.route('/help')
    def help():
        global previous_page
        previous_page = "#"
        return render_template(lang + "/faq.html", previous_page=previous_page)

    @app.route('/about')
    def about():
        global previous_page
        previous_page = "about"
        return render_template(lang + "/about.html")

    # ----------------------------------------
    # admin

    ALLOWED_EXTENSIONS = set(['png', 'htm'])

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    password = "none"

    @app.route('/administrator', methods=['GET', 'POST'])
    def admin():
        global password, adminpassword, WIFI_login, WIFI_password, floor_number_old, floor_number, userstatus
        floor_number_old = floor_number

        f = open('user.txt')

        status = f.readline()
        print(status)
        status = status[:-1]

        name = f.readline()
        print(name)
        name = name[:-1]

        second_name = f.readline()
        print(second_name)
        second_name = second_name[:-1]

        login = f.readline()
        print(login)
        login = login[:-1]

        adminpassword = f.readline()
        print(adminpassword)
        adminpassword = adminpassword[:-1]

        f.close()

        f = open('userstatus.txt')

        userstatus = f.readline()
        userstatus = userstatus[:-1]
        print("----->" + userstatus + "<-----")

        f.close()

        if userstatus == 'True':
            if request.method == 'POST':

                WIFI_login = request.form['WIFI_login']
                print(WIFI_login)
                WIFI_password = request.form['WIFI_password']
                print(WIFI_password)

                time = request.files['time']
                if time and allowed_file(time.filename):
                    time.save(os.path.join("static/time/", "time.htm"))

                about = request.files['about']
                if about and allowed_file(about.filename):
                    about.save(os.path.join("static/", "about.htm"))

                floor_number = request.form['floor_number']
                print(floor_number)

                # print(password == adminpassword)

                new_file = open('adminconfig.txt', 'w')
                new_file.write('%s\n' % WIFI_login)
                new_file.write('%s\n' % WIFI_password)
                new_file.close()

                floor_status = ['disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled',
                                'disabled', 'disabled']
                for i in range(int(floor_number)):
                    floor_status[i] = '   '
                    print(floor_status)

                new_file = open('map.txt', 'w')
                new_file.write('%s\n' % floor_number)
                for i in range(9):
                    new_file.write('%s\n' % floor_status[i])

                for i in range(9):
                    if i < int(floor_number_old):
                        new_file.write('%s\n' % request.form['floor_' + str(i + 1) + '_name'])
                    else:
                        new_file.write('Недоступно\n')

                new_file.close()

                for i in range(int(floor_number_old)):
                    map = request.files['floor_' + str(i + 1)]
                    if map and allowed_file(map.filename):
                        map.save(os.path.join("static/map/", "map" + str(i + 1) + ".png"))

                return render_template("/admininterface.html", name=name, second_name=second_name, status=status,
                                       password_error=False, WIFI_login=WIFI_login, WIFI_password=WIFI_password,
                                       floor_number=floor_number, floor_a_status=floor_1_status,
                                       floor_b_status=floor_2_status, floor_c_status=floor_3_status,
                                       floor_d_status=floor_4_status, floor_e_status=floor_5_status,
                                       floor_f_status=floor_6_status, floor_g_status=floor_7_status,
                                       floor_h_status=floor_8_status, floor_i_status=floor_9_status,
                                       floor_a_name=floor_1_name, floor_b_name=floor_2_name, floor_c_name=floor_3_name,
                                       floor_d_name=floor_4_name, floor_e_name=floor_5_name, floor_f_name=floor_6_name,
                                       floor_g_name=floor_7_name, floor_h_name=floor_8_name, floor_i_name=floor_9_name)
            else:
                return render_template("/admininterface.html", name=name, second_name=second_name, status=status,
                                       password_error=False, WIFI_login=WIFI_login, WIFI_password=WIFI_password,
                                       floor_number=floor_number, floor_a_status=floor_1_status,
                                       floor_b_status=floor_2_status, floor_c_status=floor_3_status,
                                       floor_d_status=floor_4_status, floor_e_status=floor_5_status,
                                       floor_f_status=floor_6_status, floor_g_status=floor_7_status,
                                       floor_h_status=floor_8_status, floor_i_status=floor_9_status,
                                       floor_a_name=floor_1_name, floor_b_name=floor_2_name, floor_c_name=floor_3_name,
                                       floor_d_name=floor_4_name, floor_e_name=floor_5_name, floor_f_name=floor_6_name,
                                       floor_g_name=floor_7_name, floor_h_name=floor_8_name, floor_i_name=floor_9_name)
        else:
            if request.method == 'POST':
                In_password = request.form['password']
                In_login = request.form['login']
                if In_password == adminpassword and In_login == login:
                    f = open('userstatus.txt', 'w')
                    f.write('True\n')
                    f.close()
                return render_template("/admininterface.html", name=name, second_name=second_name, status=status,
                                       password_error=False, WIFI_login=WIFI_login, WIFI_password=WIFI_password,
                                       floor_number=floor_number, floor_a_status=floor_1_status,
                                       floor_b_status=floor_2_status, floor_c_status=floor_3_status,
                                       floor_d_status=floor_4_status, floor_e_status=floor_5_status,
                                       floor_f_status=floor_6_status, floor_g_status=floor_7_status,
                                       floor_h_status=floor_8_status, floor_i_status=floor_9_status,
                                       floor_a_name=floor_1_name, floor_b_name=floor_2_name, floor_c_name=floor_3_name,
                                       floor_d_name=floor_4_name, floor_e_name=floor_5_name, floor_f_name=floor_6_name,
                                       floor_g_name=floor_7_name, floor_h_name=floor_8_name, floor_i_name=floor_9_name)
            else:
                return render_template("/adminlogin.html", name=name, second_name=second_name, status=status,
                                       password_error=False, WIFI_login=WIFI_login, WIFI_password=WIFI_password,
                                       floor_number=floor_number, floor_a_status=floor_1_status,
                                       floor_b_status=floor_2_status, floor_c_status=floor_3_status,
                                       floor_d_status=floor_4_status, floor_e_status=floor_5_status,
                                       floor_f_status=floor_6_status, floor_g_status=floor_7_status,
                                       floor_h_status=floor_8_status, floor_i_status=floor_9_status,
                                       floor_a_name=floor_1_name, floor_b_name=floor_2_name, floor_c_name=floor_3_name,
                                       floor_d_name=floor_4_name, floor_e_name=floor_5_name, floor_f_name=floor_6_name,
                                       floor_g_name=floor_7_name, floor_h_name=floor_8_name, floor_i_name=floor_9_name)
        return "error!"

    @app.route('/profile', methods=['GET', 'POST'])
    def profil():
        global adminpassword
        f = open('user.txt')

        status = f.readline()
        print(status)
        status = status[:-1]

        name = f.readline()
        print(name)
        name = name[:-1]

        second_name = f.readline()
        print(second_name)
        second_name = second_name[:-1]

        login = f.readline()
        print(login)
        login = login[:-1]

        adminpassword = f.readline()
        print(adminpassword)
        adminpassword = adminpassword[:-1]

        f.close()
        if request.method == 'POST':
            password = request.form['password']
            new_name = request.form['new_name']
            new_second_name = request.form['new_second_name']
            new_login = request.form['new_login']
            new_password = request.form['new_password']
            file = request.files['profile_photo']
            if file and allowed_file(file.filename):
                file.save(os.path.join("static/images/", "profile_photo.jpg"))

            if adminpassword == password:
                new_file = open('user.txt', 'w')
                if new_login == "admin" and new_password == "root":
                    new_file.write('default\n')
                elif new_password == "root":
                    new_file.write('bad\n')
                else:
                    new_file.write('changed\n')

                new_file.write('%s\n' % new_name)
                new_file.write('%s\n' % new_second_name)
                new_file.write('%s\n' % new_login)
                new_file.write('%s\n' % new_password)
                new_file.close()

            else:
                return render_template('/profile.html', password_error=True)
        return render_template('/profile.html', password_error=False)



def f_2():
    global istate, lmain, cap, var0, mashtab, count_frame, detect_faces_opencv, AddQ, nameMTS, personMTS, statusMTS, Rtime, Btime
    statusMTS = "Ok"
    bluure = 5
    mashtab = 0.5
    print("Thread2")
    face_cascade = cv2.CascadeClassifier('C:\CV_Start\haarcascades\haarcascade_frontalface_default.xml')
    count_frame = 0
    detect_faces_opencv = False
    flag_opencv = False
    cap = cv2.VideoCapture(0)
    var0 = 1
    # while 1:
    #     time.sleep(1)
    #     print("------")


    while True:
        _, frame = cap.read()
        count_frame += 1


        frame, face_descriptors = FaceAlgo.find_faces_in_image(frame, bluure, False)

        person_name = "no_name"
        #print('preparing for recognize')
        for face_descriptor in face_descriptors:

            #print('recognizing')
            # отрисовываем и проверяем все найденные лица
            ret, dist = FaceAlgo.compare_face(face_descriptor[0])
            #print(ret, dist)
            if ret:
                if len(ret) > 0:
                    d = face_descriptor[1]
                    cv2.putText(frame, str(str(round(dist, 2)) + " " + str(ret[2])), (d.left(), d.top()),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    #print("Похож на ", ret[2])
                    person_name = str(ret[2])

                    # evt = threading.Event()
                    # q.put((person_name, evt))
                    # print('Waiting for data to be doubled')
                    # evt.wait()

            else:
                if statusMTS == "Er":
                    print("Error")
                    continue
                # if (Btime) - (int(time.time())) > 0:
                #     print("Error")
                #     Btime -= int(time.time())
                #     continue
                else:
                    print("Create new person")
                    nameMTS = input()
                    db.add_person(nameMTS)
                    answer, personMTS = db.search_person(nameMTS)
                    FaceAlgo.name(nameMTS, personMTS)
                    frame, face_descriptors = FaceAlgo.find_faces_in_image(frame, bluure, nameMTS, True)
                    tstart = int(time.time())
                    while ((tstart+15) - (int(time.time())) > 0):
                        _, frame = cap.read()
                        frame, face_descriptors = FaceAlgo.find_faces_in_image(frame, bluure, nameMTS,True)
                        Rtime = (tstart+15) - (int(time.time()))
                        print((tstart+15) - (int(time.time())))
                    # time.sleep(8)

        if person_name != "no_name":
            print(person_name)


#q = Queue()

thread = threading.Thread(target=f_1())
#thread2 = threading.Thread(target=f_2())

thread.start()
#thread2.start()

#q.join()



