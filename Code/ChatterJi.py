import tkinter as tk
import threading
from PIL import ImageTk, Image
from playsound import playsound
root = tk.Tk()
root.title("ChatterJi")
root.overrideredirect(True)
img1 = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-Icon.png").resize((15, 15), Image.ADAPTIVE))
img = ImageTk.PhotoImage(Image.open("../Images/ChatterJi-logos.jpeg").resize((1600, 900), Image.ANTIALIAS))
root.iconphoto(False, img1)
tk.Label(root,image=img).pack()
root.after(3000, lambda: root.destroy())
def loadsound():
    playsound("../Sounds/welcome.wav")
def main():
    p1 = threading.Thread(target=loadsound,args=())
    p1.start()
    root.mainloop()
if __name__ == '__main__':
    main()
    filename='../Code/begin.py'
    exec(compile(open(filename, "rb").read(), filename, 'exec'))