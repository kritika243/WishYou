import tkinter
from tkinter import BOTH, StringVar
from PIL import Image, ImageTk

# defining main window
root = tkinter.Tk()
root.title('WishYou')
root.iconbitmap('cake.ico')
root.geometry('400x400')
root.resizable(0,0)

# defining colors and fonts
root_color = '#c2cae8'
input_color ='#f9cff2'
output_color = '#a9fbd7'
root.config(bg=root_color)

# functions

# layout
# frames
input_frame=tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=15)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

# widgets
name = tkinter.Entry(input_frame, text='enter your name', width=20)
submit = tkinter.Button(input_frame, text='Submit')
name.grid(row=0, column=0, padx=10, pady=10)
submit.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# radio buttons
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text='Normal Case',variable = case_style, value='normal', bg=root_color)
upper_button = tkinter.Radiobutton(input_frame, text='Upper Case',variable = case_style, value='upper', bg=root_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

myImage = ImageTk.PhotoImage(Image.open('teddy.png'))
image_label = tkinter.Label(output_frame, image=myImage, bg=output_color)
image_label.pack()

root.mainloop()