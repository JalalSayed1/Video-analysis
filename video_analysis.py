import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    width = int(cap.get(3)) # 3 means the width. convert to int as this returns a floating value.
    height = int(cap.get(4)) # 4 means the height. convert to int as this returns a floating value.

    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    image = np.zeros(frame.shape, np.uint8) # to make a convas same to our frame shape. np.uint8 is the type of this array (uint8 = unsigned integers)
    
    # to put the smaller frame in the convas:
    image[:height//2, :width//2] = smaller_frame # top left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # top right
    # if want more videos in the window:
    # image[height//2:, :width//2] = smaller_frame # bottom left
    # image[height//2:, width//2:] = smaller_frame # bottom right

    cv2.imshow("image", image)

    if cv2.waitKey(1) == ord("q"): # after 1 ms, if q is pressed it will break
        break

cap.release()
cv2.destroyAllWindows()

