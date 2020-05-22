from Tkinter import *
root1=Tk()
root1.geometry('550x350')
root1.title('developed by')
Label(root1,text='PROJECT TITLE:PHONEBOOK ',font='times 20 bold italic').grid(row=0,column=1)
Label(root1,text='PROJECT OF PYTHON AND DATABASE ',font='times 20 bold italic').grid(row=1,column=1)
Label(root1,text='Developed by: BALAJI G ',font='times 10 bold italic').grid(row=2,column=1)
Label(root1,text='---------------------- ').grid(row=3,column=1)
Label(root1,text='make mouse movement over this to close ').grid(row=4,column=1)
root1.geometry('600x500')

def close(e=1):
    root1.destroy()
root1.bind('<Motion>',close)    
mainloop()

