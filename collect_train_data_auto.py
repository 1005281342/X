import os
# from time import sleep
from random import randint

import cv2
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-t", "--type", default='0', help="需要采集的手势标签")
args = vars(ap.parse_args())
num_string = str(args["type"])
if num_string not in {'0', '1', '2', '3', '4', '5'}:
    raise Exception("请检查输入参数")

print("现在采集的手势分类数据是", num_string)
# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")

# Train or test
mode = 'train'
directory = 'data/' + mode + '/'

cap = cv2.VideoCapture(0)
_ = cap.set(3, 240)
_ = cap.set(4, 320)

status = False
count_index = 0
while True:
    count_index += 1
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    mapping = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five'
    }

    # 统计已存在的图片数据
    count = {'zero': len(os.listdir(directory + "/0")),
             'one': len(os.listdir(directory + "/1")),
             'two': len(os.listdir(directory + "/2")),
             'three': len(os.listdir(directory + "/3")),
             'four': len(os.listdir(directory + "/4")),
             'five': len(os.listdir(directory + "/5"))}

    # 显示文字、字幕
    cv2.putText(frame, "MODE : " + mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ZERO : " + str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "ONE : " + str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "TWO : " + str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "THREE : " + str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FOUR : " + str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "FIVE : " + str(count['five']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    # ROI坐标
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # 绘制ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64))     # 采集图像的尺寸

    cv2.imshow("Frame", frame)

    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)

    if not status:
        interrupt = cv2.waitKey(50)
    else:
        interrupt = cv2.waitKey(10)

    if interrupt & 0xFF == 27 or count_index == 1024:  # esc key
        break

    cv2.imwrite(directory + num_string + '/' + str(randint(10, 20))
                + str(count[mapping[num_string]]) + '.jpg', roi)

cap.release()
cv2.destroyAllWindows()
