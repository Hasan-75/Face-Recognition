import cv2
from mtcnn import MTCNN


def main():
    detector = MTCNN()
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        img = frame
        boxes = detector.detect_faces(img)
        for box in boxes:
            img = bound_box_draw(box, img)
        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def bound_box_draw(bb, img):
    #face
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    x, y, w, h = bb['box']

    #calculate dinamyc thickness
    thickness = int(w/30)
    if(thickness<=0):
        thickness = 1
        
    img = cv2.rectangle(img, (x, y+h), (x+w, y), red, thickness=thickness)
    img = cv2.putText(img, "face", (x,y), cv2.FONT_HERSHEY_PLAIN, thickness, green, thickness=thickness)
    #eyes
    attrs = bb['keypoints']
    img = cv2.circle(img, attrs['left_eye'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['right_eye'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['nose'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['mouth_left'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['mouth_right'], thickness, blue, thickness=-1)
    return img

if __name__ == "__main__":
    main()