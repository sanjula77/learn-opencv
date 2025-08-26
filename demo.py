import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def read_image():
    root = os.getcwd()
    imgpath = os.path.join(root, 'images', 'cat.jpg')
    img = cv.imread(imgpath)

    if img is None:
        print('Image not found at path:', imgpath)
        exit()

    # Resize image to 800x600 (width x height)
    img_resized = cv.resize(img, (800, 600))

    cv.imshow('Cat Image', img_resized)
    cv.waitKey(0)
    cv.destroyAllWindows()  # closes window after key press

def write_image():
    root = os.getcwd()
    imgpath = os.path.join(root, 'images', 'cat.jpg')
    img = cv.imread(imgpath)
    if img is None:
        print('Image not found at path:', imgpath)
        exit()
    save_path = os.path.join(root, 'images', 'cat_copy.jpg')
    cv.imwrite(save_path, img)    

def video_from_webcam():
    cap = cv.VideoCapture(0)  # 0 is usually the default camera

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv.imshow('Webcam Feed', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    #read_image()
    # write_image()
    video_from_webcam()
