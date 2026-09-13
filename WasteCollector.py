import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
import tkinter

root = tkinter.Tk()
root.title("Waste Collector Screen")
root.geometry("430x400")




def runVideo():
    template = cv2.imread('template/template.jpg')
    template = cv2.resize(template,(150,150))
    w = template.shape[1]
    h = template.shape[0]
    test = askopenfilename(initialdir = "videos")
    video = cv2.VideoCapture(test)
    msg = ''
    while(True):
            ret, frame = video.read()
            print(ret)
            if ret == True:
                cv2.imwrite("test.jpg",frame)
                img = cv2.imread("test.jpg")
                img = cv2.resize(img,(300,300))
                img2 = img.copy()
                img = img2.copy()
                method = eval('cv2.TM_CCOEFF_NORMED')
                res = cv2.matchTemplate(img,template,method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                x = min_loc[0]
                y = max_loc[0]
                x1 = min_loc[1]
                y1 = max_loc[1]
                msg = "Waste Not Detected"
                if (x-y) < 45 and (x1 - y1) < 45 :
                    msg = "Waste Detected"
                print(str(min_val)+" "+str(max_val)+" "+str(min_loc)+" "+str(max_loc))
                if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                if (x-y) < 45 and (x1 - y1) < 45 :
                    cv2.rectangle(img,top_left, bottom_right, 155, 2)
                text_label = "{}: {:4f}".format(msg, 80)
                cv2.putText(img, text_label, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.imshow('Frame', img)
                if cv2.waitKey(3) & 0xFF == ord('q'):
                    break
            else:
                break
    video.release()
    cv2.destroyAllWindows()

font = ('times', 16, 'bold')
title = Label(root, text='Geo Tracking Based Waste Collector Application',justify=LEFT)
title.config(bg='PaleGreen2', fg='Khaki4')  
title.config(font=font)           
#title.config(height=3, width=120)       
title.place(x=10,y=5)

font1 = ('times', 14, 'bold')
upload = Button(root, text="Upload Video", command=runVideo)
upload.place(x=100,y=100)
upload.config(font=font1)      
    
root.config(bg='brown')
root.mainloop()

