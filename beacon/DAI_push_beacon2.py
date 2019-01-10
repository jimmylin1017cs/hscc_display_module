import time, DAN, requests, random
import json

#from requests.utils import requote_uri


#ServerURL = 'http://IP:9999' #with no secure connection
#ServerURL = 'https://DomainName' #with SSL connection
ServerURL = 'http://140.113.199.181:9999'
Reg_addr = None #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Transmit_Boxes'
DAN.profile['df_list']=['IDF_Boxes', 'ODF_Boxes', 'IDF_SELECTOR', 'IDF_Beacon', 'IDF_Beacon2']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

#cv2.setUseOptimized(True)

#cap = cv2.VideoCapture('time_counter.flv')

def send_boxes_to_iottalk(boxes):

    #print(type(buf))
    #array = buf.tolist()
    #print(len(buf))
    boxes_information = json.dumps(boxes)
    #print(boxes_information)
    #print(data)
    #print(len(data))

    try:
        # @0: json
        DAN.push('IDF_Beacon2', boxes_information)
        #print('push')
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            #time.sleep(1)
    #time.sleep(0.2)


def main():
    
    beacon_information = list()
    boxes = dict()
    filename = '2.txt'

    while True:

        with open(filename, 'r') as beacon_file:
            s = beacon_file.readline()
            beacon_information = s.split(' ')
            #print(beacon_information[0])
            #print(beacon_information[1])
        boxes['id'] = int(2)
        boxes['x'] = float(beacon_information[0])
        boxes['y'] = float(beacon_information[1])
        send_boxes_to_iottalk(boxes)

if __name__ == '__main__':
    main()
