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

def read_video_file():
    root = os.getcwd()
    videopath = os.path.join(root, 'videos', 'sample_video.mp4')
    cap = cv.VideoCapture(videopath)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or error reading frame.")
            break

        cv.imshow('Video Playback', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv.destroyAllWindows()

# def read_and_write_single_pixels():
#     root = os.getcwd()
#     imgpath = os.path.join(root, 'images', 'cat.jpg')
#     img = cv.imread(imgpath)
#     imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#     iyePixel = imgRGB[1225, 868]
#     imgRGB[1225, 868] = [255, 0, 0]  # Change pixel to red

#     plt.figure(figsize=(10, 5))
#     plt.imshow(imgRGB)
#     plt.show()

def read_and_write_single_pixels():
    # Get image path
    root = os.getcwd()
    imgpath = os.path.join(root, 'images', 'cat.jpg')
    img = cv.imread(imgpath)

    if img is None:
        print("Error: Image not found.")
        return

    # Convert BGR → RGB for Matplotlib display
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Pixel coordinates from your screenshot (x=1226, y=824)
    x, y = 1226, 824   # x = column, y = row

    # Get original pixel value
    pixel_value = imgRGB[y, x]   # NOTE: OpenCV uses (row=y, col=x)
    print(f"Original pixel at ({x},{y}): {pixel_value}")

    # Change pixel to red
    imgRGB[y, x] = [255, 0, 0]

    # Show the updated image
    plt.figure(figsize=(10, 5))
    plt.imshow(imgRGB)
    plt.show()


if __name__ == "__main__":
    # read_image()
    # write_image()
    # video_from_webcam()
    # read_video_file()
      read_and_write_single_pixels()
