import rplidar as rp
import time
lidar = rp.RPLidar("COM3", 115200)
print(lidar.get_health())
li = lidar.iter_measurments(50000)
# print(read)


class PromobotLidar:

    def __init__(self, PORT):
        self.lidar = rp.RPLidar(PORT, 115200)

    def searchforward(self, interval):
        # interval - the range of data read values, the "field of view" of the lidar
        distance = 0
        for scan in lidar.iter_scans():
            try:
                for i in range(len(scan)):
                    if scan[i][1] >= 360-(interval/2) and scan[i][1] < interval/2:
                        distance = scan[i][2]
                        break
            except:
                continue
        return distance


lidar.clear_input()
time.sleep(1)

