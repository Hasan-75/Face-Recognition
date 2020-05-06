from mtcnn import MTCNN
import cv2

def main():
    img = cv2.imread(".\\images\\war.jpg")
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = MTCNN()
    bound_boxes = detector.detect_faces(img)
    for box in bound_boxes:
        img = bound_box_draw(box, img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def bound_box_draw(bb, img):
    #face
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    x, y, w, h = bb['box']

    #dynamic thickness
    thickness = int(w/30)
    if(thickness<=0):
        thickness = 1

    img = cv2.rectangle(img, (x, y+h), (x+w, y), red, thickness=thickness)
    img = cv2.putText(img, "face", (x,y), cv2.FONT_HERSHEY_PLAIN, thickness, green, thickness=thickness)
    #other face parts
    attrs = bb['keypoints']
    img = cv2.circle(img, attrs['left_eye'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['right_eye'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['nose'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['mouth_left'], thickness, blue, thickness=-1)
    img = cv2.circle(img, attrs['mouth_right'], thickness, blue, thickness=-1)
    return img


if __name__ == "__main__":
    main()