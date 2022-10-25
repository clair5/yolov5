import yolo_detector
import cv2
import os

file_path = "D:/yolov5/img/1.png"

dir = os.path.isfile(file_path)
print(dir)  # True                               #경로에 파일이 있는 지 확인

if dir == True:
    img = cv2.imread("D:/yolov5/img/1.png",cv2.IMREAD_UNCHANGED) #이미지 부르기
    det = yolo_detector.detect(img) #이미지 디텍팅
    print(det)
    if det is not None: #디텍팅 될 부분이 있는 지 확인
        image = yolo_detector.draw_boxes(img, det)  #디텍팅 된다면 이미지에 그리기
    cv2.imwrite("D:/yolov5/img/2.png",image) #이미지 저장하기
    #cv2.imshow('my window',image) #별도의 창으로 띄우기
    

else:
    print("failed")


#a와 b를 비교해서 늘어난 훼손 내용을 확인하는 함수 -> 추가된 내역만 리스트로 반환
def check(a, b):
    a.sort()
    b.sort()
    c = b
    for i in range(len(a)):
        if a[i] in b:
            c.remove(a[i])
    return c

#추가된 훼손 내용과 횟수를 확인하는 함수
def ncheck(c):
    d = []
    for i in range(len(b)):
        if b[i] not in d:
            d.append(b[i])
        else:
            continue
    for j in range(len(d)):
        print('%s가 %d회 감지되었습니다.' % (b[j], b.count(b[j])))

a = ['notch', 'spot', 'wornout', 'wornout']
b = ['notch', 'notch', 'spot', 'wornout', 'wornout', 'wornout', 'wornout']

if (a is None) or (b is None):
    print('정보가 없습니다.')
else:
    if len(a) == len(b):
        print('정상입니다. 반납해주세요.')
    elif len(a) < len(b):
        dams = check(a, b)
        ncheck(dams)
        print('창구를 확인해주세요.')
    else:
        print('오류입니다. 직원을 불러주세요.')
