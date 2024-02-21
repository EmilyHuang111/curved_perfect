import cv2 as cv  # Import the OpenCV library for image processing
import Detection  # Import the Process code
import Display  # Import the Display code

try:  # Start a try block to catch any potential exceptions
    #https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html example 1 for all the code below
    # Define a function called DisplayVid
    def display_video():
        # Open the default camera (index 0)
        cap = cv.VideoCapture(0)
        # Start a loop to continuously capture frames from the camera
        while cap.isOpened():
            # Read a frame from the camera
            ret, frame = cap.read()
            # Process the frame using the process_image function from the Process module
            Detection.detect_lines(frame)
            # Display the processed frame using the display_image function from the Display module
            Display.display_image(frame)
        # Close all OpenCV windows
        cv.destroyAllWindows()
    display_video()

except:  # If an exception occurs, execute the following block of code
    print("Stopping the program")  # Print a message indicating that the program is stopping

# Execute the following block whether an exception occurs or not
finally:
    exit()  # Exit the program
