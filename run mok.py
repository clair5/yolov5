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
import cv2
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
        file = "D:\\yolov5\\img\\"+str(count)+".png"
        print(file)
        blob.download_to_filename(file)
        if count == 5:
            break



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



