import cv2, time

# number of webcams in the argument
video = cv2.VideoCapture(0)

#a = 1


# Creating a frame to show face
while True:
    #a += 1
    check, frame = video.read()

    #print(check)
    #print(frame)

    blackNwhite = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)

    cv2.imshow("Capturing", blackNwhite) # to se color change variable blackNwhite to frame

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
#print(a)
video.release()
cv2.destroyAllWindows()
