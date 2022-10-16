import cv2, time
from cvzone.FaceMeshModule import FaceMeshDetector

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector(maxFaces=1)


    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]

            w, _ = detector.findDistance(pointLeft, pointRight)
            W = 6.3

            f = 480
            d = (W * f) / w

            if d < 35:
                for x in range(0, 6):
                    time.sleep(0.5)
                    success, img = cap.read()
                    img, faces = detector.findFaceMesh(img, draw = False)
                    if faces:
                        face = faces[0]
                        pointLeft = face[145]
                        pointRight = face[374]
                        w, _ = detector.findDistance(pointLeft, pointRight)
                        d = (W * f) / w
                        if x == 5:
                            print("Woah! You're a little too close to the screen buddy!")
                            time.sleep(60)
                        elif d >= 35:
                            break