import time, DAN, requests, random
import json
import numpy as np
import cv2
import base64
from ast import literal_eval
import time

#from requests.utils import requote_uri


#ServerURL = 'http://IP:9999' #with no secure connection
#ServerURL = 'https://DomainName' #with SSL connection
ServerURL = 'http://140.113.86.143:9999'
Reg_addr = None #if None, Reg_addr = MAC address

DAN.profile['dm_name']='MODEL_ALL'
DAN.profile['df_list']=['ODF_ALL']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

#cap = cv2.VideoCapture('time_counter.flv')

def receive_frame_from_iottalk():

    #print('start receive frame from iottalk')
    try:
        data = DAN.pull('ODF_ALL')
        if data != None:
            print("pull")
            print(data[0])
            all_boxes_information = data[0].split('|')
            all_boxes_information_size = len(all_boxes_information)
            boxes_information = all_boxes_information[0]
            enable_name = all_boxes_information[all_boxes_information_size - 1]
            #print(person_information)
            tmp_boxes = json.loads(boxes_information)
            tmp_enable_name = json.loads(enable_name)
            print(tmp_boxes)
            print(tmp_enable_name)

            tmp_beacon = list()
            for i in range(1, all_boxes_information_size - 1):
                tmp_beacon.append(json.loads(all_boxes_information[i]))

            print(tmp_beacon)
            
            #tmp_nparray = np.array(tmp_array)
            #tmp_buf = tmp_nparray.astype('uint8')
            #frame = cv2.imdecode(tmp_buf, 1)
            #cv2.imshow('Receive',frame)
            #cv2.waitKey(1)

            return (tmp_boxes, tmp_enable_name, tmp_beacon)

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            #time.sleep(1)    

    #time.sleep(0.2)
    return None
    
