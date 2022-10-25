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
import os
from tokenize import Name
import torch

cred = credentials.Certificate('hustar-9eeb8-firebase-adminsdk-alcry-ae50a8362d.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'hustar-9eeb8',
    'storageBucket': 'hustar-9eeb8.appspot.com'
})

count = 0
bucket = storage.bucket()
ds =bucket.list_blobs(prefix='my_folder/')
print('bucket'.__len__())
for blob in ds:
    if(not blob.name.endswith("/")):
        count+=1
        print(f'Downloading file [{blob.name}]',count) 
        file2 = "C:\\Users\\h\\Desktop\yolov5 (2)\\yolov5\\img\\"+str(count)+".png"
        #file = "C:\\Users\\h\\Desktop\\yolov5\\img\\"+str(count)+".png"
        print(file2)
        blob.download_to_filename(file2)
        if count == 5:
            break