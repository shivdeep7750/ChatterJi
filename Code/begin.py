

from tkinter import *
from tkinter import simpledialog
import tkinter as Tk
from PIL import ImageTk, Image
from tkinter import messagebox
import Code.src.managedb as mdb
import Code.src.managedb_rooms as rooms
import paho.mqtt.client as mqtt
import random
import cv2
import base64
import json
from PIL import Image as im
import numpy as np
import ast
from datetime import datetime
random.seed(datetime.now())
randseed=random.randint(1, 100000)
from tkinter import filedialog as fd
listbox=None
ended = False
user='NONE'
room=None
import hashlib
def on_message(client, userdata, message):
    global chat1
    global listbox1
    listbox1.configure(state='normal')
    msg = eval(message.payload.decode("utf-8"))
    fetchdata = {'data': msg['data'],
            'sender': msg['sender']}
    print(str(fetchdata))
    hash = hashlib.md5(str(fetchdata).encode())
    print(msg['hash'])
    print(str(hash))
    if(str(hash)!= msg['hash'] and False):
        listbox1.insert(END, "[INTRUSION DETECTED] " + msg['sender'] + "'s messege may have been compromised! Messege was \"" + msg['data'] + "\"\n")
    else:
        if(msg['rand']==str(randseed) and msg['rand1']=='NULL'):
            pass
        elif((msg['rand1']!='NULL') and msg['rand']!=str(randseed) ):
            file = msg['data1']
            print(file)
            decodeit = open(str('Downloads/File_from_'+msg['sender']+str(datetime.now().strftime("%b-%d-%Y-%H-%M-%S"))+'.'+msg['rand1']), 'wb')
            decodeit.write(base64.b64decode((file)))
            decodeit.close()
            listbox1.insert(END,msg['data']+" was shared by "+msg['sender']+"\n")
        else:
            listbox1.insert(END,"REPLY from "+msg['sender']+"- "+msg['data']+"\n")
    listbox1.configure(state='disabled')
    del hash


broker_address = "e04df2a58e0a4f528230883d969a19ec.s1.eu.hivemq.cloud"
port = 8883
global client
client = mqtt.Client()
client.on_message = on_message
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("publicUN", "123publicPASS")
client.connect(broker_address, port)
client.loop_start()

def on_click3():
    data = {'data': "Left the room",
            'sender': user}
    hash = hashlib.md5(str(data).encode())
    print(str(data))
    print(str(hash))
    data = {'data': "Left the room",
            'sender': user,
            'rand': str(randseed),
            'rand1': 'NULL',
            'hash': str(hash)}
    client.publish(room, str(data))
    client.disconnect()
    exit(0)
def upload():
    filename = fd.askopenfilename()
    with open(filename, "rb") as img_file:
        data1 = base64.b64encode(img_file.read())
    data = {'data': "File Sent : "+filename,
            'sender': user}
    hash = hashlib.md5(str(data).encode())
    ext=filename[::-1]
    i=ext.find('.')
    ext=ext[0:i]
    ext=ext[::-1]

    data = {'data': "File Shared : "+filename,
            'sender': user,
            'rand' : str(randseed),
            'rand1': ext,
            'data1': data1,
            'hash': str(hash)}
    client.publish(room, str(data))

def on_click2():
    global chat1
    global client
    #client.loop_start()
    listbox1.configure(state='normal')
    data = str(chat1.get())
    listbox1.insert(END, "Me: "+data+"\n")
    listbox1.yview(END)
    listbox1.configure(state='disabled')
    data = {'data': data,
            'sender': user}
    hash=hashlib.md5(str(data).encode())
    print(str(data))
    print(str(hash))
    data={'data':str(chat1.get()),
          'sender':user,
          'rand': str(randseed),
          'rand1': 'NULL',
          'hash':str(hash)}
    client.publish(room, str(data))
    del hash
    chat1.delete(0,"end")
def on_click():
    on_click2()
def conn(addr):
    global client
    client.subscribe(addr)
    data = {'data': "Hey, I am here!!",
            'sender': user}
    hash = hashlib.md5(str(data).encode())
    print(str(data))
    print(str(hash))
    data = {'data': "Hey, I am here!!",
            'sender': user,
            'rand': str(randseed),
            'rand1': 'NULL',
            'hash': str(hash)}
    client.publish(room, str(data))

def main3():
    global client
    client.loop_start()
    global m
    m.destroy()
    window=Tk.Tk()
    window.title('ChatterJi')
    window['bg'] = 'white'
    window.overrideredirect(True)
    window.geometry("1600x900")
    img1 = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-Icon.png").resize((15, 15), Image.ADAPTIVE))
    #img = ImageTk.PhotoImage(Image.open("..\Images\ChatterJi-logos_transparent.png").resize((1600, 600), Image.ANTIALIAS))
    window.iconphoto(False, img1)
    window.configure(background="grey")
    #background_label = Label(window, image=img)
    #background_label.grid(column=0,row=0, padx=0, pady=0)
    global listbox1
    global chat1
    listbox1 = Text(window, wrap=WORD, width="139", height="30", font=("Courier", 14),bg='#b3ecff',fg='red')
    listbox1.grid(column=0, row=0, padx=1, pady=1)
    chat1 = Tk.Entry(window)
    chat1['width'] = 150
    chat1['relief'] = Tk.GROOVE
    chat1['bg'] = '#f5f6f7'
    chat1['fg'] = 'red'
    chat1['font'] = ("Courier", 12)
    chat1.grid(column=0, row=1, padx=1, pady=1)
    # Button
    send = Tk.Button(window, command=on_click, text="Send",width=30,height=2,bg='#2bad50')
    send['relief'] = Tk.GROOVE
    send['activebackground'] = '#404040'
    send['padx'] = 1
    send['font'] = ("Courier", 15)
    send.grid(column=0, row=2, padx=5, pady=15)
    #background_label.grid(row=1, column=0,columnspan=3, padx=0, pady=0)
    button40 = Tk.Button(window,text="Leave the Room", height=1, width=30, command=on_click3,bg='red')
    button40.grid(row=3)

    button41 = Tk.Button(window, text="Upload", height=1, width=30, command=upload, bg='white')
    button41.grid(row=4)
    conn(room)
    #######sample
    listbox1.configure(state='normal')
    listbox1.tag_configure("center", justify='center')
    listbox1.insert(END,"Connected to "+room+" as "+user+"\n\n\n\n")
    #listbox1.tag_configure("center", justify='left')
    listbox1.configure(state='disabled')

    window.mainloop()
#################################
def Newprocess():
    global room
    answer = simpledialog.askstring("Ghost Room", "Give your room a name\n", parent=m)
    if (answer == ''):
        Newprocess()
    elif (answer==None):
        exit(0)
    db = rooms.ManageDB()
    room=str(answer)
    data1={
        "room":room,
        "creator":user
    }
    room = str(answer+" by "+user)
    db.save_data(data1)
    main3()
def join():
    global listbox
    data=listbox.get(ANCHOR)
    global room
    room=data
    i=data.find(' by ')
    #room=data[0:i]
    data1={
        "room":data,
        "creator":user
    }
##############################################    ##process furthur
    main3()
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
    db = rooms.ManageDB()
    v=db.view_records()
    listbox = Listbox(m,width="75",height="10",selectmode="SINGLE",font=("Arial", 12))
    for i in range(len(v)):
        listbox.insert(i,v[i][0]+" by "+v[i][1])
    listbox.pack()
    w7 = Tk.Label(m, text="\n")
    w7.pack()
    button5 = Tk.Button(m, text='Join the room', height=5, width=45, command=join,bg="green").pack()
    button4 = Tk.Button(m, text='Change of plans, GTG!', height=5, width=45, command=exit,bg="red")
    button4.pack()

def main2():
    global m
    global w
    w = Tk.Label(m, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    global button3
    button3 = Tk.Button(m, text='Change of plans, GTG!', height=5, width=45, command=exit,bg="red")
    global  w0
    w0=Tk.Label(m,text="Welcome : "+user+"\n",font=("Arial", 15))
    w.pack()
    w0.pack()
    button3.pack()
    global button1
    global button2
    button1 = Tk.Button(m, text='Get me brand NEWWWW room!', height=5, width=45, command=Newprocess,bg="grey")
    button2 = Tk.Button(m,text="I'll Manage with an existing room", height=5, width=45, command=oldroom)
    button1.pack()
    button2.pack()
########################################
def get_data(user):
    data = {
        "user": str(user)
    }
    return data

def check_username(user):
    if len(user)>=4 and user!='NONE':
        return True
    return False

def process():
    global ended
    global user
    if(user=='NONE'):
        exit(0)
    db = mdb.ManageDB()
    stats = get_data(user)
    db.save_data(stats)
    db.view_records()
    ended = True
    filename='../Code/RoomSelector.py'
    ###########delete all
    #exec(compile(open(filename, "rb").read(), filename, 'exec'))
    button1.destroy()
    button2.destroy()
    w.destroy()
    main2()
def start_process():
    button40 = Tk.Button(m,text="Quit!", height=5, width=45, command=quit)
    button1.destroy()
    button2.destroy()
    global user
    w = Tk.Label(m, text="Quick guide:\nNote: Name should be atleast 4 character long\n\n",font=("Helvetica",13))
    w.pack()
    button40.pack()
    answer1 = simpledialog.askstring("ChatterJi", "Give yourself a name\n", parent=m)
    if(answer1==None):
        exit(0)
    user = str(answer1)
    if(check_username(user)==True and answer1):
        process()
    button40.destroy()
    w.destroy()
    if(check_username(user)==False):
        messagebox.showinfo("OOPS!", "Get yourself a good username please😢")
        start_process()

def main():
    global m
    m = Tk.Tk()
    m.title('ChatterJi')
    m.geometry("1600x900")
    img1 = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-Icon.png").resize((15, 15), Image.ADAPTIVE))
    img = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-logos_transparent.png").resize((1000, 700), Image.ANTIALIAS))
    m.iconphoto(False, img1)
    m.configure(background="grey")
    C = Canvas(m, bg="white", height=250, width=300)
    background_label = Label(m, image=img)
    background_label.place(x=0, y=-226, relwidth=1, relheight=1)
    C.pack()
    global w
    w = Tk.Label(m, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    w.pack()
    global button1
    global button2
    button1 = Tk.Button(m, text='Get me a room!', height=5, width=45, command=start_process,bg="grey")
    button2 = Tk.Button(m,text="Quit!", height=5, width=45, command=quit)
    button1.pack()
    button2.pack()
    m.overrideredirect(True)
    m.mainloop()

main()
client.disconnect()
client.loop_stop()
