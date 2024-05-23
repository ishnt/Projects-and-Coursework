import cv2

# Function to handle mouse events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at ({x}, {y})")

# Open the video file
cap = cv2.VideoCapture("E:\heatmap\gg.mp4")

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error reading video file")
    exit()

# Create a window to display the video
cv2.namedWindow("Video")

# Set mouse callback function
cv2.setMouseCallback("Video", click_event)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("End of video")
        break

    # Display the frame
    cv2.imshow("Video", frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
