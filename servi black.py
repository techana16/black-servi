import tkinter as tk
import serial

gui = tk.Tk ()

gui.geometry("600x600")
arm = serial.Serial('com30', 9600)
#START OBUCHENIE
def start():
    global states
    states = []

def remember():
    global states
    global msg
    states.append(msg)


def play():
    global states
    for op in states :
        arm.write(op.encode())
        time.sleep(sld.get())
        time.sleep(s1.get())
        time.sleep(s2.get())
        time.sleep(n1.get())
        time.sleep(under.get())
#slider
s1= tk.Scale(gui,from_=-9, to=9  , orient= tk.HORIZONTAL)
s1.place(x= 120, y=100 )

s2= tk.Scale(gui,from_=-9, to=9 )
s2.place(x= 50, y=200 )

sld= tk.Scale(gui,from_=-9, to=9 )
sld.place(x= 150, y=200 )

n1= tk.Scale(gui,from_=-9, to=9)
n1.place(x= 250, y=200 )

under = tk.Scale(gui,from_=-9, to=9  , orient= tk.HORIZONTAL)
under.place(x= 120, y=350 )

#zaglavie
texts = tk.Label(gui, text= 'Servi black ' ,  foreground="black"  )
texts.config( font=('times', 28, 'italic'  ))
texts.place (x=210, y= 30)

#obuchenie
clear = tk.Button (gui, text='START ', bg = 'cyan', command= start  ,height= 2, padx= 9  )
clear.place (x=30, y=450)

remember= tk.Button (gui, text='REMEMBER ', bg = 'cyan', command= remember ,height= 2, padx= 2 )
remember.place (x=145, y= 450)

playb = tk.Button(gui, text='REPEAT', bg = 'cyan' , command=play , height= 2 , padx=9 )
playb.place(x=270, y=450)

gui.mainloop()
