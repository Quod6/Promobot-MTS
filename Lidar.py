import rplidar as rp
import time
lidar = rp.RPLidar("COM3", 115200)
print(lidar.get_health())
li = lidar.iter_measurments(50000)
# print(read)

class promobotLidar(object):

    def __init__(self, PORT):
        self.lidar = rp.RPLidar(PORT, 115200)

    def SearchForward(self):
        for scan in lidar.iter_scans():
            try:
                for i in range(len(scan)):
                    if scan[i][1] >= 0 and scan[i][1] < 2:
                        distance = scan[i][2]
                        break
            except:
                pass
        return distance



lidar.clear_input()
time.sleep(1)

