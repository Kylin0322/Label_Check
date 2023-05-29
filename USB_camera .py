#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File        :USB_camera .py
@Time        :2023/05/26 14:03:31
@Author      :Yu Wang
@Version     :1.0
@Contact     :@qq.com
@Description :
'''

import cv2
from datetime import datetime

class camera_USB():
    def __init__(self) -> None:
        self.camera=None
        self.file_name=""
        pass

    def init(self):
        self.camera=cv2.VideoCapture(0)
    
    def capture_image(self):

        if self.camera == None:
            self.init()
        result, img = self.camera.read()
        
        if result:
            return img
        else:
            return None
        
    def capture_image_to_file(self,file_name="Cpa_YYYYMMDDHHmmSS.png"):
        '''
        '''
        if self.camera == None:
            self.init()

        if file_name=="Cpa_YYYYMMDDHHmmSS.png":
           from datetime import datetime
           T= datetime.now().strftime("%Y%m%d%H%M%S")
           self.file_name="cap_" + T + ".png"
           print(self.file_name)
           pass

        result, img = self.camera.read()

        if result:
            cv2.imwrite(filename=self.file_name,img=img)
            return img
        else:
            return None
        

if __name__ == '__main__':
    cam= camera_USB()
    cam.init()
    cam.capture_image_to_file()
    

