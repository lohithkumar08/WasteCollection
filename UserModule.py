from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import cv2

main = tkinter.Tk()
main.title("User Waste Photo Upload Screen")
main.geometry("900x400")



global username_entry
global location_entry
global desc_entry
global photo_entry
global path

global name
global location
global desc
global photo
 
name = StringVar()
location = StringVar()
desc = StringVar()
photo = StringVar()

def upload():
    global path
    path = filedialog.askopenfilename(initialdir = "images")
    photo_entry.delete(0,END)
    photo_entry.insert(0,path)

def save():
    s1 = name.get()
    s2 = location.get()
    s3 = desc.get()
    s4 = photo.get()
    img = cv2.imread(path)
    cv2.imwrite("template/template.jpg",img)
    messagebox.showinfo("Details Accepted", "Your image and details sent to waste collectors")
    

font = ('times', 15, 'bold')
title = Label(main, text='Geo Tracking of Waste and Triggering Alerts and Mapping Areas with High Waste Index',justify=LEFT)
title.config(bg='brown', fg='white')  
title.config(font=font)           
title.config(height=3, width=80)       
title.place(x=0,y=5)

font1 = ('times', 14, 'bold')
l1 = Label(main, text="Username * ")
l1.place(x=100,y=100)
l1.config(font=font1)  
username_entry = Entry(main, textvariable=name)
username_entry.place(x=250,y=100)

l2 = Label(main, text="Location * ")
l2.place(x=100,y=150)
l2.config(font=font1)  
location_entry = Entry(main, textvariable=location)
location_entry.place(x=250,y=150)

l3 = Label(main, text="Description * ")
l3.place(x=100,y=200)
l3.config(font=font1)  
desc_entry = Entry(main, textvariable=desc)
desc_entry.place(x=250,y=200)

l4 = Label(main, text="Photo Path * ")
l4.place(x=100,y=250)
l4.config(font=font1)  
photo_entry = Entry(main, textvariable=photo)
photo_entry.place(x=250,y=250)

uploadbutton = Button(main, text="Upload Photo", command=upload)
uploadbutton.place(x=420,y=250)
uploadbutton.config(font=font1)



savebutton = Button(main, text="Save Request", command=save)
savebutton.place(x=200,y=300)
savebutton.config(font=font1)

main.config(bg='brown')
main.mainloop()

