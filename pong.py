from tkinter import *
import time

wid = 800
hei = 500

class Ball():
    def __init__(self,size):
        self.size = size
        self.ball  = area.create_oval(wid//2,hei//2,wid//2+size,hei//2+size,fill="orange")
        self.xchange = 4
        self.ychange = 4

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

class Paddle():

    WIDTH = 20
    HEIGHT = 80
    def __init__(self,x,y,upkey,downkey):
        self.paddle = area.create_rectangle(x,y,x+self.WIDTH,y+self.HEIGHT,fill="red")
        self.ychange = 0
        area.bind_all(upkey,self.upmove)
        area.bind_all(downkey,self.downmove)

    def upmove(self,event):
        self.ychange = -4
    def downmove(self,event):
        self.ychange = 4  

    def draw(self):
        area.move(self.paddle,0,self.ychange)
        position = area.coords(self.paddle)[1]
        if position <0 or position >hei-self.HEIGHT:
            self.ychange = 0


main = Tk()

area = Canvas(main,width=wid,height=hei)
area.create_line(wid//2,0,wid//2,hei)
area.create_oval(wid//2-60,hei//2-60,wid//2+60,hei//2+60)
area.create_text(wid//2,20,text="0 : 0",font=("arial",20,"bold"),fill="blue")
ball = Ball(20)
paddle1 = Paddle(5,hei//2-40,"w","s")
paddle2 = Paddle(wid-25,hei//2-40,"<KeyPress-Up>","<KeyPress-Down>")
ball.move()
area.pack()
main.update()

while 1:
    ball.move()
    paddle1.draw()
    paddle2.draw()
    main.update()
    time.sleep(0.01)

#main.mainloop()