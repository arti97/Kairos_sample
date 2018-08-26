#!/usr/bin/env python3

import requests
import json
import cv2
import numpy as np
import base64

cap = cv2.VideoCapture(0)


def main(img, gallery_name):
    url = 'https://api.kairos.com/recognize'
    headers = {
			'Content-Type' : 'application/json',
            'app_id' :  'bb56ba1f',
            'app_key' : '6128569136e2861ef49460da3f8b4685' }
			
    body = {
            'image': img,
            'gallery_name': 'test_gallery' }

    r = requests.post(url, headers=headers, json=body)
    d = json.loads(r.text)
    print(r.json()['images'][0]['transaction']['subject_id'])
    return r.json()['images'][0]['transaction']['status'] == 'success' if True else False 
    #print(r.text)
	
def opencv():
	print("IN OPENCV----------------")
	while True:
		
		ret, frame = cam.read()
		cv2.imshow("test", frame)
		if not ret:
			break
		k = cv2.waitKey(1)
		if k%256 == 27:
			print("ESCAPE-------------")
			break
		elif k%256 == 32:
			#img_name = "opencv_frame_{}.png".format(img_counter)
			cv2.imwrite('face.png',frame)
			main(convertImage(frame), 'test_gallery')
			print("SAVED------------------")		
					
	cam.release()
	cv2.destroyAllWindows()

def convertImage(img):
	ret, buffer = cv2.imencode('.jpg', img)
	returnimage = base64.b64encode(buffer).decode('ascii')
	return returnimage
	
if __name__ == '__main__':
    opencv()