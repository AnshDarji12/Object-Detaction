import os 
import cv2 
import time 
import uuid

image_path = "CollectedImages"

lebels = ['Hello','Yes','No','Thanks','I love you','Please','Fuck you']

number_of_images = 10

for label in lebels:
    img_path = os.path.join(image_path,label)
    os.makedirs(img_path)
    
    cap=cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(4)
    
    for imnum in range(number_of_images):
        ret,frame=cap.read()
        imagename = os.path.join(image_path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow("frame",frame)
        time.sleep(3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
        
    cap.release()