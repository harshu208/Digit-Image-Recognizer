from keras.models import load_model
import numpy as np
model = load_model('mnist.h5')
def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)


import subprocess

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox
import os
#This creates the main window of an application
root = Tk()
root.title("Digit Recognizer")
toolBar =Menu(root)
root.configure(background='Grey',menu=toolBar)

def clear_canvas():
    canvas.delete('all')

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()

def open_img():
    browse_file()
    imgname=os.path.basename(file_path)
    loaded_img=ImageTk.PhotoImage(Image.open(file_path).resize((500,500),resample=0))
    canvas.create_image(10,10, anchor=NW, image=loaded_img) 
    canvas.loaded_img = loaded_img
    
def predict_image():
    i = Image.open(file_path)
    digit,accuracy = predict_digit(i)
    accuracy = str((int(accuracy*100)))
    digit = str(digit)
    pred_details.configure(text = digit + " with " + accuracy + " % surety")

def open_mspaint():
    subprocess.Popen(['C:\\Windows\\System32\\mspaint.exe'])

canvas = Canvas(root, width = 500, height = 500)  
pred_details = Label(text="Please load an Image", font=("Comic Sans MS", 30))
predict_btn = Button(text = "Predict Digit", command = predict_image)
clear_btn = Button(text = "Clear Image", command = clear_canvas)

# Grid structure
canvas.grid(row=0, column=0, pady=2, sticky=W, )
pred_details.grid(row=0, column=1,pady=2, padx=2)
predict_btn.grid(row=1, column=1, pady=2, padx=2)
clear_btn.grid(row=1, column=0, pady=2)

subMenu = Menu(toolBar,tearoff=0)
toolBar.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label='Open Digit Image',command= open_img)
subMenu.add_command(label="Draw a Digit (MS Paint)", command=open_mspaint)
subMenu.add_command(label="Exit",command=root.destroy)




root.mainloop()
