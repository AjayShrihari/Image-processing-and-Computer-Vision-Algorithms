import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# import cv2
import cv2
import numpy as np


def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        points.append((x, y))

# cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Frame", mouse_drawing)
points = []
frame = cv2.imread('rubiks.jpg', cv2.IMREAD_COLOR)

while True:
    # _, frame = cap.read()
    for center_position in points:
        cv2.circle(frame, center_position, 15, (0, 0, 255), -1)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('d'):
        break
    
# cap.release()
cv2.destroyAllWindows()
print(len(points))
print(points)
np.save("Points2.npy", np.array(points))
