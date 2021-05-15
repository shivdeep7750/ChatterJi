from tkinter import *
import tkinter as Tk
from tkinter import simpledialog
from PIL import ImageTk, Image
import Code.src.managedb_rooms as rooms
db=rooms.ManageDB()
ended = False
import guli
user = guli.GuliVariable("usershared").get()
listbox=None
m = Tk.Tk()

def Newprocess():
    global room
    answer = simpledialog.askstring("Ghost Room", "Give your room a name\n", parent=m)
    if (answer == ''):
        Newprocess()
    elif (answer==None):
        exit(0)
    room = str(answer)
    exit(0)
def join():
    global listbox
    data=listbox.get(ANCHOR)
    join(data)
    pass
def oldroom():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    w.destroy()
    w0.destroy()
    w1 = Tk.Label(m, text="\n\n\n\n\n\n")
    w1.pack()
    w4=Tk.Label(m,text="Welcome : "+user+"\n",font=("Arial", 15))
    w4.pack()
    global listbox
    v=db.view_records()
    listbox = Listbox(m,width="75",height="10",selectmode="SINGLE",font=("Arial", 12))
    for i in range(len(v)):
        listbox.insert(i,v[i])
    listbox.pack()
    w7 = Tk.Label(m, text="\n")
    w7.pack()
    button5 = Tk.Button(m, text='Join the room❤', height=5, width=45, command=join,bg="green").pack()
    button4 = Tk.Button(m, text='Change of plans, GTG!💔', height=5, width=45, command=exit,bg="red")
    button4.pack()

def main():
    global m
    m.title('Room Selector-ChatterJi')
    m.geometry("1600x900")
    img2 = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-Icon1.png").resize((15, 15), Image.ADAPTIVE))
    img = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-logos_transparent.png").resize((1000, 700), Image.ANTIALIAS))
    m.iconphoto(False, img2)
    m.configure(background="grey")
    C = Canvas(m, bg="white", height=250, width=300)
    background_label = Label(m, image=img)
    background_label.place(x=0, y=-226, relwidth=1, relheight=1)
    C.pack()
    global w
    w = Tk.Label(m, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    global button3
    button3 = Tk.Button(m, text='Change of plans, GTG!💔', height=5, width=45, command=exit,bg="red")
    global  w0
    w0=Tk.Label(m,text="Welcome : "+user+"\n",font=("Arial", 15))
    w.pack()
    w0.pack()
    button3.pack()
    global button1
    global button2
    button1 = Tk.Button(m, text='Get me brand NEWWWW room!😁', height=5, width=45, command=Newprocess,bg="grey")
    button2 = Tk.Button(m,text="I'll Manage with an existing room😫", height=5, width=45, command=oldroom)
    button1.pack()
    button2.pack()
    m.overrideredirect(True)
    m.mainloop()
if __name__=='__main__':
    main()
