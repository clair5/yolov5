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

file_path = "C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/1.jpg"

dir = os.path.isfile(file_path)
print(dir)  # True                               #경로에 파일이 있는 지 확인

if dir == True:  # 디렉토리 다운 받은 파일 확인하고 훼손된 부분 리스트 추가 
    
    img = cv2.imread("C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/1.jpg",cv2.IMREAD_UNCHANGED) #이미지 부르기
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
    cv2.imwrite("C:/Users/HUSTAR09/Desktop/yolov5 (3)/yolov5/img/2.jpg",image) #이미지 저장하기
    #cv2.imshow('my window',image) #별도의 창으로 띄우기
  

#c_name이 아래 코드에서 리스트 b에 해당하는 내용-현재 찍은 사진에서 훼손 내역-인데
#해당 내용을 파이어베이스 데이터베이스로 올라가는 코드를 못 짬
    

else:
    print("failed") 

'''
훼손 내역 확인 코드
'''
"""
#내용부터 비교를... 해야된다 이거지
# #a와 b를 비교해서 늘어난 훼손 내용을 확인하는 함수 -> 추가된 내역만 리스트로 반환
# def check(a, b):
#     a.sort()
#     b.sort()
#     c = b
#     for i in range(len(a)):         #c에 b를 넣어서 a와 b가 겹치는 부분을 c에서 삭제
#         if a[i] in b:
#             c.remove(a[i])
#     # print(c)
#     return c

# #추가된 훼손 내용과 횟수를 확인하는 함수
# def ncheck(b):
#     d = []
#     for i in range(len(b)):         #a와 b에서 차이가 발생한 것 중 중복 제거
#         if b[i] not in d:
#             d.append(b[i])
#         else:
#             continue
#     # print(d)
#     for j in range(len(d)):         #각 훼손마다 몇 번 발생했는지 확인
#         print('%s가 %d회 감지되었습니다.' % (d[j], b.count(d[j])))
#길이가 같은 경우 a가 b에 포함되는지 확인하는 함수
"""



def icheck(a, b):                   # 리스트 길이 같을때 체크하는 함수 
    a.sort()
    b.sort()
    c = b
    for i in range(len(a)):         #a와 b에서 내용의 차이가 존재하는지 확인
        if a[i] in b:
            c.remove(a[i])          #a와 b가 같다면 True 반환
        else:                       #a와 b가 다르면 False 반환
            continue
    if c is None:
        return True
    else:
        return False

        
# 파이어베이스에 리스트 받아오기 
#이 부분은 나중에 파이어베이스 데이터베이스에서 리스트를 받아오는 걸로 변경해야 됨
a = ['ripped']
b = ['notch', 'notch', 'spot', 'wornout', 'wornout', 'wornout', 'wornout']


# 훼손확인하는 함수 
if (b is None):                   
    print('정보가 없습니다.')
else:
    if len(a) == len(b):                       
        ch = icheck(a, b)
        if ch == True:
            print('정상입니다. 반납해주세요.')
        else:
            print('훼손이 추가되었습니다. 창구를 확인해주세요.')
    elif len(a) < len(b):
        # dams = check(a, b)
        # ncheck(dams)
        print('훼손이 늘었습니다. 창구를 확인해주세요.')
    else:
        print('오류입니다. 직원을 불러주세요.')
