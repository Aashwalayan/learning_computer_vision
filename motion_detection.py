import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        1.3,
        5
    )

    for(x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y +h),
            (255, 0, 0),
            2
        )

        face_x = x + w // 2
        face_y = y + h // 2

        screen_x = frame.shape[1] // 2
        screen_y = frame.shape[0] // 2

        # if face_x < screen_x:
        #     print("Left")
        # elif face_x > screen_x:
        #     print("Right")
        # else:
        #     print("Center")

        cv2.circle(
            frame,
            (face_x, face_y),
            3,
            (120, 143, 50),
            -1
        )

    cv2.imshow("Face Detector", frame)

    key = cv2.waitKey(1)

    if key == 27 or key == ord('q'):
        break

    if key == ord('s'):
        cv2.imwrite("photo.jpg", frame)

cam.release()
cv2.destroyAllWindows()