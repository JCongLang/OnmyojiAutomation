# -*- encoding=utf8 -*-
__author__ = "Leonjack"

from airtest.core.api import *
import random

auto_setup(__file__)



# 提取屏幕分辨率
screen_width, screen_height = 1050, 600

def finishTouch(screen_width, screen_height):
    # 生成随机的 x 和 y 坐标
    for _ in range(2):
        random_x = random.randint(-int(250), int(250))
        random_y = random.randint(-int(200), int(200))
        point_x = screen_width + random_x
        point_y = screen_height + random_y
        print(point_x)
        print(point_y)
        touch((point_x, point_y))
        print("finish_touch_end")
def failureTouch():
    # 生成随机的 x 和 y 坐标
    for _ in range(1):
        point_x = random.randint(int(1350), int(1590))
        point_y = random.randint(int(300), int(800))
        print(point_x)
        print(point_y)
        touch((point_x, point_y))
        print("failure_touch_end")
i = 1
while(1):
    print("Start challenge for " + str(i) + " times.")
    centor_point = wait(Template(r"tpl1725889063125.png", record_pos=(0.403, 0.218), resolution=(1600, 900)))
    print(centor_point)
    match_result = find_all(Template(r"tpl1725889063125.png", record_pos=(0.403, 0.218), resolution=(1600, 900)))
    a, b, c, d = match_result[0]['rectangle']
    width = random.randint(-int((c[0] - a[0]) / 2), int((c[0] - a[0]) / 2))
    height = random.randint(-int((b[1] - a[1]) / 2), int((b[1] - a[1]) / 2))
    touch((centor_point[0] + width, centor_point[1] + height))

    sleep(26 + random.uniform(-1, 1))
#     failureTouch()
    if exists(Template(r"tpl1725872395192.png", record_pos=(0.004, 0.117), resolution=(1600, 900))):
        print("First template found")
        finishTouch(screen_width, screen_height)
    
    elif exists(Template(r"tpl1725953013228.png", record_pos=(0.013, -0.128), resolution=(1600, 900))):
        print("Failure template found")
        failureTouch()
    else:
        print("No template found")
        sleep(10)
        failureTouch()
    print("Finish")
    sleep(random.randint(0, 1))
 
    i += 1


