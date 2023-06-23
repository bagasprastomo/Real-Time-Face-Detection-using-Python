import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def detect_bounding_box(vid):
    grayscale = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    #Set the minimal size to detect any faces
    faces = face_classifier.detectMultiScale(grayscale, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        #Set the border around the faces
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #Put the "Face found!" text above the square
        cv2.putText(vid, "Face found!", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
    return faces

while True:

    #Read frames from the video
    result, video_frame = webcam.read()
    if result is False:
        break
        #Break the loop if the frame doesn't read

    faces = detect_bounding_box(video_frame)
    #Apply the function to create a border around face

    cv2.imshow("Realtime Face Detection", video_frame)
    #Display a webcam window and set the title to "Realtime Face Detection"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()