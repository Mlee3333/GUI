from tkinter import *

wid = 800
hei = 500

class Ball():
    def __init__(self,size):
        self.size = size
        self.ball  = area.create_oval(wid//2,hei//2,wid//2+size,hei//2+size,fill="orange")
        self.xchange = 0.04
        self.ychange = 0.04

    def move(self):
        area.move(self.ball,self.xchange,self.ychange)
        pos = area.coords(self.ball)
        if pos[0] <=0:
            self.xchange = -self.xchange
        if pos[0] >=wid:
            self.xchange = -self.xchange
        if pos[1] <=0:
            self.ychange = -self.ychange
        if pos[1] >=hei:
            self.ychange = -self.ychange

main = Tk()

area = Canvas(main,width=wid,height=hei)
area.create_line(wid//2,0,wid//2,hei)
area.create_oval(wid//2-60,hei//2-60,wid//2+60,hei//2+60)
area.create_text(wid//2,20,text="0 : 0",font=("arial",20,"bold"),fill="blue")
ball = Ball(20)
ball.move()
area.pack()
main.update()

while 1:
    ball.move()
    main.update()

#main.mainloop()