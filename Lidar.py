import rplidar as rp
import cv2
import time
import threading as tr

class PromobotLidar():

    flagdraw = False

    def __init__(self, PORT):
        self.lidar = rp.RPLidar(PORT, 115200)
        '''while 1:
            try:
                print(PORT)
                #self.lidar = rp.RPLidar(PORT, 115200)
            except rp.RPLidarException as e:
                print(e)
                print("Подключите Лидар или укажите другой порт")
                PORT1 = upper(input("Укажите порт: "))
                if PORT1 == "":
                    continue
                else:
                    PORT = PORT1
                    print(PORT)
                    continue
        '''


    def searchforward(self, interval):
        distance = []
        for scan in self.lidar.iter_scans():
            try:
                for i in range(len(scan)):
                    if scan[i][1] >= 360-(interval/2) or scan[i][1] < interval/2:
                        print("Adding", scan[i][2], "angle", scan[i][1])
                        distance.append(scan[i][2])
                        break
                    print("skip", scan[i][1])
            except Exception as E:
                print(E)
        return distance

    def startdrawmap(self, weight, hight):
        if self.flagdraw == False:
            self.flagdraw = True
        while self.flagdraw:
            pass

    def stopdrawmap(self):
        self.flagdraw = False


if __name__ == '__main__':
    lidar1 = PromobotLidar("COM3")
    r = lidar1.searchforward(90)
    print(r)