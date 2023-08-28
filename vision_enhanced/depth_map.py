import threading
import time

import cv2
import numpy as np
import keyboard
import pickle

import win32gui

from InterceptionWrapper import InterceptionMouseState, InterceptionMouseStroke, InterceptionKeyState, \
    InterceptionKeyStroke
from AutoHotPy import AutoHotPy
import win32api
import win32con
from screen_capture import ScreenCapture


class Settings:
    numDisparities = 0
    blockSize = 0
    preFilterType = 0
    preFilterSize = 0
    preFilterCap = 0
    textureThreshold = 0
    uniquenessRatio = 0
    speckleRange = 0
    speckleWindowSize = 0
    disp12MaxDiff = 0
    minDisparity = 0


if __name__ == '__main__':

    def draw_line(x1=0, y1=0, x2=0, y2=0):
        coordinates = []

        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x1, y1

        error, t = el / 2, 0

        coordinates.append([x, y])

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            coordinates.append([x, y])

        return coordinates


    def smooth_move(autohotpy, x, y):
        flags, hcursor, (startX, startY) = win32gui.GetCursorInfo()
        coordinates = draw_line(startX, startY, startX + 1, startY)
        print(startX, startY)
        # for dot in coordinates:
        # time.sleep(0.001)
        # x += 1
        # if x % 2 == 0 and x % 3 == 0:
        #   time.sleep(0.001)
        autohotpy.moveMouseToPosition(1, 0)


    def turn(auto_py, x, y, _direction):
        # print('WOLK DAN STRIT EN TORN KORNAR')

        time.sleep(0.5)
        stroke = InterceptionMouseStroke()
        #
        # stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
        # auto_py.sendToDefaultMouse(stroke)
        # time.sleep(0.02)
        # stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
        # auto_py.sendToDefaultMouse(stroke)
        # time.sleep(0.02)
        #
        # stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
        # auto_py.sendToDefaultMouse(stroke)
        # time.sleep(0.02)
        # stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
        # auto_py.sendToDefaultMouse(stroke)
        # time.sleep(0.02)
        #
        stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
        auto_py.sendToDefaultMouse(stroke)
        # time.sleep(0.02)
        # smooth_move(auto_py, x, y)  # @TODO ЧТОБЫ НИЧЕГО НЕ ТЕКЛО
        print("moveMouseToPosition", _direction)
        auto_py.moveMouseToPosition(_direction, 0)
        # stroke.state = InterceptionMo5useState.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
        # auto_py.sendToDefaultMouse(stroke)
        time.sleep(0.02)
        print('READY TO SCREENSHOT')


    def nothing(x):
        pass


    def save_settings(settings: Settings):
        file_name = 'settings.pkl'
        with open(file_name, 'wb') as f:
            pickle.dump(settings, f)


    def open_settings():
        file_name = 'settings.pkl'
        s: Settings
        with open(file_name, 'rb') as f:
            s = pickle.load(f)
            print(s.numDisparities)


    cv2.namedWindow('disp', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('disp', 600, 600)

    cv2.createTrackbar('numDisparities', 'disp', 1, 17, nothing)
    cv2.setTrackbarMin('numDisparities', 'disp', 1)

    cv2.createTrackbar('blockSize', 'disp', 5, 50, nothing)
    cv2.createTrackbar('preFilterType', 'disp', 1, 1, nothing)
    cv2.createTrackbar('preFilterSize', 'disp', 2, 25, nothing)

    cv2.createTrackbar('preFilterCap', 'disp', 5, 62, nothing)
    cv2.setTrackbarMin('preFilterCap', 'disp', 1)

    cv2.createTrackbar('textureThreshold', 'disp', 10, 100, nothing)
    cv2.createTrackbar('uniquenessRatio', 'disp', 15, 100, nothing)
    cv2.createTrackbar('speckleRange', 'disp', 0, 100, nothing)
    cv2.createTrackbar('speckleWindowSize', 'disp', 3, 25, nothing)
    cv2.createTrackbar('disp12MaxDiff', 'disp', 5, 25, nothing)
    cv2.createTrackbar('minDisparity', 'disp', 5, 25, nothing)

    # Creating an object of StereoBM algorithm
    stereo = cv2.StereoBM_create()
    # stereo = cv2.StereoSGBM_create(minDisparity=1)

    settings = Settings()
    keyboard.on_press_key('space', lambda x: save_settings(settings))
    keyboard.on_press_key('v', lambda x: open_settings())
    left_eye_coords = (200, 200)
    right_eye_coords = (203, 200)
    clicked = False
    direction = -1

    screenCap = ScreenCapture('Asterios')


    def exitAutoHotKey(autohotpy, event):
        autohotpy.stop()


    left_index = 0
    right_index = 0

    while not keyboard.is_pressed('esc'):
        # Capturing and storing left and right camera images
        # retL, imgL = CamL.read()
        # retR, imgR = CamR.read()
        if keyboard.is_pressed('w'):
            print("W ", clicked)
            clicked = not clicked

        _, _, (x, y) = win32gui.GetCursorInfo()
        if clicked:
            auto_py = AutoHotPy()
            auto_py.registerExit(auto_py.ESC, exitAutoHotKey)
            # auto_py.start()
            auto_py_thread = threading.Thread(target=auto_py.start)
            auto_py_thread.start()
            time.sleep(0.02)
            direction = -direction
            turn(auto_py, x, y, direction)
            screenshot1 = screenCap.capture_screen()[0]
            print('SHOT!!!!', 1)
            Left_nice = cv2.cvtColor(screenshot1, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'test_images_stereopairs/left/{left_index}.jpg', Left_nice)
            left_index += 1
            # Left_nice = cv2.imread('test_images_stereopairs/3.jpg', cv2.IMREAD_GRAYSCALE)
            direction = -direction
            turn(auto_py, x + 1, y, direction)
            screenshot2 = screenCap.capture_screen()[0]
            print('SHOT!!!!', 2)
            Right_nice = cv2.cvtColor(screenshot2, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'test_images_stereopairs/right/{right_index}.jpg', Right_nice)
            right_index += 1
            # Right_nice = cv2.imread('test_images_stereopairs/4.jpg', cv2.IMREAD_GRAYSCALE)
        else:
            time.sleep(0.016 * 3)
            Left_nice = cv2.imread(f'test_images_stereopairs/left/{left_index}.jpg', cv2.IMREAD_GRAYSCALE)
            Right_nice = cv2.imread(f'test_images_stereopairs/left/{right_index}.jpg', cv2.IMREAD_GRAYSCALE)
            left_index += 1
            right_index += 1

            if left_index >= 35:
                left_index = 0
                right_index = 0

        # pyautogui.mouseDown()

        # imgR_gray = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
        # imgL_gray = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)

        # Applying stereo image rectification on the left image
        # Left_nice = cv2.remap(imgL_gray,
        #                       Left_Stereo_Map_x,
        #                       Left_Stereo_Map_y,
        #                       cv2.INTER_LANCZOS4,
        #                       cv2.BORDER_CONSTANT,
        #                       0)
        #
        # # Applying stereo image rectification on the right image
        # Right_nice = cv2.remap(imgR_gray,
        #                        Right_Stereo_Map_x,
        #                        Right_Stereo_Map_y,
        #                        cv2.INTER_LANCZOS4,
        #                        cv2.BORDER_CONSTANT,
        #                        0)

        # Updating the parameters based on the trackbar positions
        numDisparities = cv2.getTrackbarPos('numDisparities', 'disp') * 16
        blockSize = cv2.getTrackbarPos('blockSize', 'disp') * 2 + 5
        preFilterType = cv2.getTrackbarPos('preFilterType', 'disp')
        preFilterSize = cv2.getTrackbarPos('preFilterSize', 'disp') * 2 + 5
        preFilterCap = cv2.getTrackbarPos('preFilterCap', 'disp')
        textureThreshold = cv2.getTrackbarPos('textureThreshold', 'disp')
        uniquenessRatio = cv2.getTrackbarPos('uniquenessRatio', 'disp')
        speckleRange = cv2.getTrackbarPos('speckleRange', 'disp')
        speckleWindowSize = cv2.getTrackbarPos('speckleWindowSize', 'disp') * 2
        disp12MaxDiff = cv2.getTrackbarPos('disp12MaxDiff', 'disp')
        minDisparity = cv2.getTrackbarPos('minDisparity', 'disp')

        settings.numDisparities = numDisparities
        settings.blockSize = blockSize
        settings.preFilterType = preFilterType
        settings.preFilterSize = preFilterSize
        settings.preFilterCap = preFilterCap
        settings.textureThreshold = textureThreshold
        settings.uniquenessRatio = uniquenessRatio
        settings.speckleRange = speckleRange
        settings.speckleWindowSize = speckleWindowSize
        settings.disp12MaxDiff = disp12MaxDiff
        settings.minDisparity = minDisparity

        stereo.setNumDisparities(numDisparities)
        stereo.setBlockSize(blockSize)
        stereo.setPreFilterType(preFilterType)
        stereo.setPreFilterSize(preFilterSize)
        stereo.setPreFilterCap(preFilterCap)
        stereo.setTextureThreshold(textureThreshold)
        stereo.setUniquenessRatio(uniquenessRatio)
        stereo.setSpeckleRange(speckleRange)
        stereo.setSpeckleWindowSize(speckleWindowSize)
        stereo.setDisp12MaxDiff(disp12MaxDiff)
        stereo.setMinDisparity(minDisparity)

        # Calculating disparity using the StereoBM algorithm
        disparity = stereo.compute(Left_nice, Right_nice)
        # NOTE: Code returns a 16bit signed single channel image,
        # CV_16S containing a disparity map scaled by 16. Hence it
        # is essential to convert it to CV_32F and scale it down 16 times.

        # Converting to float32
        disparity = disparity.astype(np.float32)

        # Scaling down the disparity values and normalizing them
        disparity = (disparity / 16.0 - minDisparity) / numDisparities

        # Displaying the disparity map
        cv2.imshow("disp", disparity)

        # Close window using esc key
        if cv2.waitKey(1) == 27:
            break
