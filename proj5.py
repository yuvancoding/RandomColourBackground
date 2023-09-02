from tkinter import *
import random 
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {'Color' : ['Green', 'Yellow', 'Purple', 'Red', 'Blue', 'Black', 'Pink', 'Gray', 'Brown', 'Darkblue']}

def bg_color():
    random_number = random.randint(0 , 9)
    print(dictionary['Color'][random_number])
    root.configure(background=dictionary['Color'][random_number])
    
btn=Button(root, text="Click me",command=bg_color)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()