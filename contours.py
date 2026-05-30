import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     # BLUE
    lower_blue = (100, 150, 50)
    upper_blue = (140, 255, 255)

    # RED (two ranges because red wraps around HSV)
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)

    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)

    # GREEN
    lower_green = (40, 70, 70)
    upper_green = (80, 255, 255)

    # YELLOW
    lower_yellow = (20, 100, 100)
    upper_yellow = (35, 255, 255)

    # ORANGE
    lower_orange = (10, 100, 100)
    upper_orange = (20, 255, 255)

    # PURPLE
    lower_purple = (125, 50, 50)
    upper_purple = (155, 255, 255)

    # PINK
    lower_pink = (145, 50, 50)
    upper_pink = (170, 255, 255)

    # WHITE
    lower_white = (0, 0, 200)
    upper_white = (180, 40, 255)

    # BLACK
    lower_black = (0, 0, 0)
    upper_black = (180, 255, 50)

    # GRAY
    lower_gray = (0, 0, 50)
    upper_gray = (180, 50, 200)

    # BROWN
    lower_brown = (10, 100, 20)
    upper_brown = (20, 255, 200)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()