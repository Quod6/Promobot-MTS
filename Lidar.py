import rplidar as rp
import time


class PromobotLidar():

    def __init__(self, PORT):
        self = rp.RPLidar(PORT, 115200)

    def searchforward(self, interval):
        """Interval - the range of data read values, the "field of view" of the lidar"""
        distance = 0
        read = self.iter_scans()
        for scan in self.iter_scans():
            try:
                for i in range(len(scan)):
                    if scan[i][1] >= 360-(interval/2) and scan[i][1] < interval/2:
                        distance = scan[i][2]
                        break
            except:
                continue
        return distance




if __name__ == '__main__':
    lidar1 = PromobotLidar("COM3")
    r = lidar1.searchforward(2)
    print(r)