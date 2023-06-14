import USB_camera


if __name__ == '__main__':
    cam = USB_camera.camera_USB()
    cam.init()
    cam.capture_image_to_file()
