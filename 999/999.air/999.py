# -*- encoding=utf8 -*-
__author__ = "Leonjack"

from airtest.core.api import *
import random

auto_setup(__file__)


def finishTouch():
    # 生成随机的 x 和 y 坐标
    for _ in range(2):
        point_x = random.randint(int(1350), int(1590))
        point_y = random.randint(int(300), int(800))
        print(point_x)
        print(point_y)
        touch((point_x, point_y))
        print("finish_touch_end")
        sleep(random.uniform(0, 1))
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
    try:
        centor_point = wait(Template(r"tpl1726076059186.png", record_pos=(0.418, 0.21), resolution=(1600, 900)))
        print(centor_point)
    except:
        print("No centor_point found")
        sleep(5)
        failureTouch()
    
    match_result = find_all(Template(r"tpl1726076059186.png", record_pos=(0.418, 0.21), resolution=(1600, 900)))
    a, b, c, d = match_result[0]['rectangle']
    width = random.randint(-int((c[0] - a[0]) / 2), int((c[0] - a[0]) / 2))
    height = random.randint(-int((b[1] - a[1]) / 2), int((b[1] - a[1]) / 2))
    touch((centor_point[0] + width, centor_point[1] + height))

    sleep(50 + random.uniform(-1, 1))
#     failureTouch()
    if exists(Template(r"tpl1726076238766.png", record_pos=(-0.003, -0.128), resolution=(1600, 900))):
        print("First template found")
        finishTouch()
    
    else:
        print("No template found")
        sleep(5)
        failureTouch()
    print("Finish")
    sleep(random.randint(0, 1))
 
    i += 1


