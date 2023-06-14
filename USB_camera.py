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
import os
import config


class camera_USB():
    def __init__(self) -> None:
        pass

    def init(self):
        self.cf = config.config()
        self.cf.get_config_file()

        self.camera = None
        self.file_name = ""
        self.file_save_path = self.cf.c1['Path'].get('file_save_path')
        self.file_backup_path = self.cf.c1['Path'].get('file_backup_path')
        self.camera_index = self.cf.c1['Setting'].getint('camera_index')
        self.backup_picture = self.cf.c1['Setting'].getboolean('backup_picture')

        self.camera = cv2.VideoCapture(self.camera_index)

    def capture_image(self):

        if self.camera == None:
            self.init()
        result, img = self.camera.read()

        if result:
            return img
        else:
            return None

    def capture_image_to_file(self, file_name="Cpa_YYYYMMDDHHmmSS.png"):
        '''
        '''
        if self.camera == None:
            self.init()

        if file_name == "Cpa_YYYYMMDDHHmmSS.png":
            from datetime import datetime
            T = datetime.now().strftime("%Y%m%d%H%M%S")
            self.file_name = "cap_" + T + ".png"
            print(self.file_name)
            pass

        result, img = self.camera.read()

        if result:
            save_path = os.path.join(self.file_save_path, self.file_name)
            print("save_path:", save_path)
            cv2.imwrite(filename=save_path, img=img)

            # banckup image
            if self.backup_picture:
                save_path = os.path.join(self.file_backup_path, self.file_name)
                print("save_path:", save_path)
                try:
                    cv2.imwrite(filename=save_path, img=img)
                except:
                    print("backup image error")
                finally:
                    pass

            return img
        else:
            return None


if __name__ == '__main__':

    cam = camera_USB()
    cam.init()
    cam.capture_image_to_file()
