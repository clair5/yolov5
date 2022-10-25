from cgitb import strong
from http import client
from pydoc import cli
import firebase_admin
from firebase_admin import credentials , firestore , storage
import numpy as np
import cv2
from requests import request
import requests as req
import urllib.request
from PIL import Image
import yolo_detector
import torch
import os


cred = credentials.Certificate('test-54670-firebase-adminsdk-71fxn-f226c2f6a0.json')
firebase_admin.initialize_app(cred,{
    'storageBucket': 'test-54670.appspot.com'
})
count = 0
bucket = storage.bucket()
ds =bucket.list_blobs(prefix='my_folder/')
print('bucket'.__len__())
for blob in ds:
    if(not blob.name.endswith("/")):
        print(f'Downloading file [{blob.name}]',count) 
        count+=1
        file = "C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/"+str(count)+".png"
        print(file)
        blob.download_to_filename(file)
        if count == 5:
            break

file_path = "C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/1.png"

dir = os.path.isfile(file_path)
print(dir)  # True                               #경로에 파일이 있는 지 확인

if dir == True:
    
    img = cv2.imread("C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/1.png",cv2.IMREAD_UNCHANGED) #이미지 부르기
    det = yolo_detector.detect(img) #이미지 디텍팅
    print(det)
    if det is not None: #디텍팅 될 부분이 있는 지 확인
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
                if pen >= 0.1:      #정확도가 0.7 이상인 경우에만 클래스 추가
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
        image = yolo_detector.draw_boxes(img, det)  #디텍팅 된다면 이미지에 그리기
    cv2.imwrite("C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/2.png",image) #이미지 저장하기
    #cv2.imshow('my window',image) #별도의 창으로 띄우기
    

#c_name이 아래 코드에서 리스트 b에 해당하는 내용-현재 찍은 사진에서 훼손 내역-인데
#해당 내용을 파이어베이스 데이터베이스로 올라가는 코드를 못 짬
    

else:
    print("failed")


'''
훼손 내역 확인 코드
'''

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

        

#이 부분은 나중에 파이어베이스 데이터베이스에서 리스트를 받아오는 걸로 변경해야 됨
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
