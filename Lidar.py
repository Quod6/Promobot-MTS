import rplidar as rp
from PIL import Image as img
import numpy as np
import time
import threading as tr

class PromobotLidar():

    flagdraw = False

    def __init__(self, PORT):
        self.lidar = rp.RPLidar(PORT, 115200)
        '''
        while 1:
            try:
                print(PORT)
                self.lidar = rp.RPLidar(PORT, 115200)
            except Exception as e:
                print(e)
                print("Подключите Лидар или укажите другой порт")
                PORT1 = input("Укажите порт: ").upper()
                if PORT1 == "":
                    continue
                else:
                    PORT = PORT1
                    print(PORT)
                    continue
            else:
                break
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

    def startdrawmap(self, width, height):
        if self.flagdraw == False:
            self.flagdraw = True
        map = img.new('RGB', (width, height), (0, 0, 120))
        centerX = int(width/2)
        centerY = int(height/2)
        while self.flagdraw:
            map.show()

    def stopdrawmap(self):
        self.flagdraw = False


if __name__ == '__main__':
    lidar1 = PromobotLidar("COM3")
    r = lidar1.startdrawmap(800, 600)
    print(r)