import cv2
from random import randrange
#load data
#trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose image
webcam = cv2.VideoCapture(1)



while True:
    successful_frame_read, frame = webcam.read()

    #convert to greyscale
    #greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #detect faces
    #face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

    #Draw a rectangle around the Face
    #for (x, y, w, h) in face_coordinates:
        #cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0, 10))
    
    #Display the image with the faces spotted
    cv2.imshow('Face detector', frame)
    key = cv2.waitKey(1)

    #stop if Q is pressed
    if key==81 or key==113:
        break

webcam.release()
print("Execution completed")
