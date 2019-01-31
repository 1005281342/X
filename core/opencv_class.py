import cv2
import numpy as np
import copy
import math


class GestureRecognitionWithOpenCV(object):

    def __init__(self):
        # parameters
        self.cap_region_x_begin = 0.5  # start point/total width
        self.cap_region_y_end = 0.8  # start point/total width
        self.threshold = 60  # BINARY threshold
        self.blur_value = 41  # GaussianBlur parameter
        self.bg_sub_threshold = 50
        self.learning_rate = 0

        # variables
        self.is_bg_captured = 0  # bool, whether the background captured
        self.trigger_switch = False  # if true, keyborad simulator works

        # not must
        self.print_threshold_warning = "! Changed threshold to "
        self.three = 3

        #
        self.bg_model = None

    def print_threshold(self, thr):
        print(self.print_threshold_warning + str(thr))

    def remove_bg(self, frame):
        fg_mask = self.bg_model.apply(frame, learningRate=self.learning_rate)
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        # res = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

        kernel = np.ones((3, 3), np.uint8)
        fg_mask = cv2.erode(fg_mask, kernel, iterations=1)
        res = cv2.bitwise_and(frame, frame, mask=fg_mask)
        return res

    def calculate_fingers(self, res, drawing):  # -> finished bool, cnt: finger count
        #  convexity defect
        hull = cv2.convexHull(res, returnPoints=False)
        if len(hull) > self.three:
            defects = cv2.convexityDefects(res, hull)
            if not (defects is None):  # avoid crashing.   (BUG not found)

                cnt = 0
                for i in range(defects.shape[0]):  # calculate the angle
                    s, e, f, d = defects[i][0]
                    start = tuple(res[s][0])
                    end = tuple(res[e][0])
                    far = tuple(res[f][0])
                    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                    if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                        cnt += 1
                        cv2.circle(drawing, far, 8, [211, 84, 0], -1)
                return True, cnt
        return False, 0

    def run_main(self):

        camera = cv2.VideoCapture(0)
        camera.set(10, 200)
        cv2.namedWindow('trackbar')
        cv2.createTrackbar('trh1', 'trackbar', self.threshold, 100, self.print_threshold)

        print("""
    README
    B -> 捕获的背景
    R -> 重置背景
    N -> 激活触发器
    T -> 按键测试
        """)

        while camera.isOpened():
            ret, frame = camera.read()
            threshold = cv2.getTrackbarPos('trh1', 'trackbar')
            frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
            frame = cv2.flip(frame, 1)  # flip the frame horizontally
            cv2.rectangle(frame, (int(self.cap_region_x_begin * frame.shape[1]), 0),
                          (frame.shape[1], int(self.cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
            cv2.imshow('original', frame)

            #  Main operation
            if self.is_bg_captured == 1:  # this part wont run until background captured
                img = self.remove_bg(frame)
                img = img[0:int(self.cap_region_y_end * frame.shape[0]),
                          int(self.cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
                cv2.imshow('mask', img)

                # convert the image into binary image
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (self.blur_value, self.blur_value), 0)
                cv2.imshow('blur', blur)
                ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
                cv2.imshow('ori', thresh)

                # get the contours
                thresh1 = copy.deepcopy(thresh)
                _, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                length = len(contours)
                max_area = -1
                if length > 0:
                    for i in range(length):  # find the biggest contour (according to area)
                        temp = contours[i]
                        area = cv2.contourArea(temp)
                        if area > max_area:
                            max_area = area
                            ci = i
                    res = contours[ci]
                    hull = cv2.convexHull(res)
                    drawing = np.zeros(img.shape, np.uint8)
                    cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
                    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

                    is_finish_cal, cnt = self.calculate_fingers(res, drawing)
                    if self.trigger_switch is True:
                        if is_finish_cal is True and 0 < cnt <= 4:  # 4
                            print(cnt+1, 'finger')
                            # app('System Events').keystroke(' ')  # simulate pressing blank space

                cv2.imshow('output', drawing)

            # Keyboard OP
            k = cv2.waitKey(10)
            if k == 27:  # press ESC to exit
                break
            elif k == ord('b'):  # press 'b' to capture the background
                self.bg_model = cv2.createBackgroundSubtractorMOG2(0, self.bg_sub_threshold)
                self.is_bg_captured = 1
                print('!!!Background Captured!!!')
            elif k == ord('r'):  # press 'r' to reset the background
                self.bg_model = None
                self.trigger_switch = False
                self.is_bg_captured = 0
                print('!!!Reset BackGround!!!')
            elif k == ord('n'):
                self.trigger_switch = True
                print('!!!Trigger On!!!')
            elif k == ord('t'):
                print('hello')


if __name__ == '__main__':
    C = GestureRecognitionWithOpenCV()
    C.run_main()
