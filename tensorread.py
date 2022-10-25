from tokenize import Name
import yolo_detector
import cv2
import torch
import numpy as np

#img = cv2.imread("C:/Users/HUSTAR09/Desktop/book/try/images/img001.jpg",cv2.IMREAD_UNCHANGED)
file_path = "C:\\Users\\h\\Desktop\\yolov5 (2)\\yolov5\\img\\1.png"
img2 = cv2.imread(file_path,cv2.IMREAD_UNCHANGED)


det = yolo_detector.detect(img2)
print(det)

if det is not None:             #디텍팅된 게 있으면 아래를 실행
    lend = len(det)             #det 길이 받아오기
    c_name = []
    cnt = 0
    while True:
        if cnt == lend:         #카운트가 det 길이와 같으면 탈출
            break
        else:
            per = det[cnt].tolist()
            pen = per[4]        #해당 카운트의 정확도를 받음
            nam = det[cnt][5]   #해당 카운트의 클래스를 받음
            if pen >= 0.7:      #정확도가 0.7 이상인 경우에만 클래스 추가
                if torch.eq(nam,torch.tensor(0.)):
                    c_name.append("notch")
                elif torch.eq(nam,torch.tensor(1.)):
                    c_name.append("ripped")
                elif torch.eq(nam,torch.tensor(2.)):
                    c_name.append("spot")
                elif torch.eq(nam,torch.tensor(3.)):
                    c_name.append("wornout")
                cnt += 1
            else:               #정확도가 0.7 미만인 경우
                cnt += 1        #카운트를 올리고 while문 다시 돌기
                continue

    image = yolo_detector.draw_boxes(img2, det)
cv2.imshow('my window',image)
key = cv2.waitKey()
print(c_name, cnt)
#파일에 클래스 추가
tensor_try = open("ttry.txt", "w", encoding="utf8")
print(c_name, file=tensor_try)
tensor_try.close()