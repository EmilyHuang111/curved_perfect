import cv2 as cv
#https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/ example 1
def display_image(image):
    # Create a window with the specified name and make it resizable
    cv.namedWindow("Detected Curved Lines", cv.WINDOW_NORMAL)

    # Display the input image in the created window
    cv.imshow("Detected Curved Lines", image)

    # Wait for a millisecond for a key press event before closing the window
    cv.waitKey(delay=1)
