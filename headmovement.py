import numpy as np
import time
import cv2

cap = cv2.VideoCapture(0) # Links to user's default webcam
colour_threshold = 100000 # Colour saturation threshold for different locations --> change accordingly

# Counter system to detect times that each colour is prsent in the frame
# Blue for right ear // Green for left ear // etc.
blue_counter = 0
green_counter = 0

while True:
    # Read each frame of the video feed
    _, frame = cap.read()
    
    # Convert default opencv BGR to hsv --> more suitable than RGB due to colour saturation values
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Define range of blue colour to trigger the counter
    lower_blue = np.array([51,101,51])
    upper_blue = np.array([130,255,255])

    # Define range of green colour to trigger the counter
    lower_green = np.array([50,100,50])
    upper_green = np.array([70,255,255])

    # Create threshold for the image to detect blue colour
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_count = blue_mask.sum()

    # Create threshold for the image to detect green colour
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green_count = green_mask.sum()

    # Print when blue is detected every 1 second
    if(blue_count > colour_threshold):
        blue_counter += 1
        print(blue_counter, 'Blue is detected')
        time.sleep(1)

    # Print when green is detected every 1 second
    if(green_count > colour_threshold):
        green_counter += 1
        print(green_counter, 'Green is detected')
        time.sleep(1)

    cv2.imshow('frame', frame)
    cv2.imshow('green mask', green_mask)

    exit = cv2.waitKey(5) & 0xFF
    if exit == 27:
        break