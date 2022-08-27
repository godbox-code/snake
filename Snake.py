from random import randint
import re
from time import sleep
from tkinter import *
from tkinter import ttk


class Snake():
    eating = False
    test1 = "green"
    game_status = 1
    new_direction = [1,0] 
    snakelist = [[100, 100, 1, 0], [80, 100, 1, 0]] # [head][tail]
    bodylist  = [[80, 100, 1, 0], [90, 100, 1, 0]]
    
    

    def __init__(self, canvas, grid):
        self.canvas = canvas
        self.grid  = grid
        self.fruit = Fruit(canvas)

    def start(self):
        self.game_status = 2
        self.canvas.create_rectangle(self.get_rec_points([self.snakelist[0][0], self.snakelist[0][1]]), fill='green', outline='green', tags='head') 
        self.canvas.create_rectangle(self.get_rec_points([self.snakelist[1][0], self.snakelist[1][1]]), fill='green', outline='green', tags='tail')
        for body in self.bodylist:
            self.canvas.create_rectangle(self.get_rec_points([body[0], body[1]]), fill=self.test1, outline=self.test1, tags='body')
        
    def move(self):
        if self.eating == True:
            if self.snakelist[0][0]%self.grid == 0 and self.snakelist[0][1]%self.grid == 0: 
                self.bodylist.append(self.snakelist[0][:])
                self.snakelist[1][2], self.snakelist[1][3] =  self.bodylist[0][2], self.bodylist[0][3]
                self.canvas.delete("body")
                for body in self.bodylist:
                    self.canvas.create_rectangle(self.get_rec_points([body[0], body[1]]), fill=self.test1, outline=self.test1, tags='body')
                self.snakelist[0][2], self.snakelist[0][3] = self.new_direction
                self.eating = False
                self.fruit.make()
            self.canvas.move('head', self.snakelist[0][2], self.snakelist[0][3])
        else:
            if self.snakelist[0][0]%self.grid == 0 and self.snakelist[0][1]%self.grid == 0: 
                self.bodylist.append(self.snakelist[0][:])
                self.bodylist.pop(0)
                self.snakelist[1][2], self.snakelist[1][3] =  self.bodylist[0][2], self.bodylist[0][3]
                #print(self.snakelist)
                self.canvas.delete("body")
                for body in self.bodylist:
                    self.canvas.create_rectangle(self.get_rec_points([body[0], body[1]]), fill=self.test1, outline=self.test1, tags='body')
                self.snakelist[0][2], self.snakelist[0][3] = self.new_direction
            self.canvas.move('head', self.snakelist[0][2], self.snakelist[0][3])
            self.canvas.move('tail', self.snakelist[1][2], self.snakelist[1][3])
            self.fruit_colision()
        self.position_update()
        self.dead()
        #print(self.snakelist[0][0], self.snakelist[0][1])
        return self.dead()

    def dead(self):
        if self.snakelist[0][0] < 10 or self.snakelist[0][0] > MainCanvasClass.framesize[0]-10 or self.snakelist[0][1] < 10 or self.snakelist[0][1] > MainCanvasClass.framesize[1]-10:
            return 1 # hit wall --- dead
        if [self.snakelist[0][0], self.snakelist[0][1]] == [self.snakelist[1][0], self.snakelist[1][1]]:
            print([self.snakelist[0][0], self.snakelist[0][1]], [self.snakelist[1][0], self.snakelist[1][1]])
            return 1 # hit tail --- dead
        for bit in self.bodylist:
            if [self.snakelist[0][0], self.snakelist[0][1]] == [bit[0], bit[1]]:
                return 1 # hit body --- dead
        return 2
    
    def fruit_colision(self):
        a = Fruit.fruit_location 
        b = [ self.snakelist[0][0]+(self.snakelist[0][2]*10), self.snakelist[0][1]+(self.snakelist[0][3]*10) ]
        if a == b:
            self.eating = True
            return 
        return

    def keyup(self, event):
        if self.game_status == 2:
            if [self.snakelist[0][2],self.snakelist[0][3]] == [0, 1]:
                return
            self.new_direction = [0, -1]
            return
        else:
            return

    def keydown(self, event):
        if self.game_status == 2:
            if [self.snakelist[0][2],self.snakelist[0][3]] == [0, -1]:
                return
            self.new_direction = [0, 1]
            return
        else:
            return

    def keyleft(self, event):
        if self.game_status == 2:
            if [self.snakelist[0][2],self.snakelist[0][3]] == [1, 0]:
                return
            self.new_direction = [-1, 0]
            return
        else:
            return

    def keyright(self, event):
        if self.game_status == 2:
            if [self.snakelist[0][2],self.snakelist[0][3]] == [-1, 0]:
                return
            self.new_direction = [1, 0]
            return
        else:
            return

    def get_rec_points(self, position):
        return [position[0]+(self.grid/2), position[1]+(self.grid/2), position[0]-(self.grid/2), position[1]-(self.grid/2)]

    def position_update(self):
        self.snakelist[0][0] += self.snakelist[0][2]
        self.snakelist[0][1] += self.snakelist[0][3]
        if self.eating == False:
            self.snakelist[1][0] += self.snakelist[1][2]
            self.snakelist[1][1] += self.snakelist[1][3]

class Fruit:
    fruit_location=[]
    
    def __init__(self, canvas):
        self.canvas = canvas

    def make(self):
        self.canvas.delete("fruit")
        self.new_location()
        self.canvas.create_oval(self.get_oval_points(self.fruit_location), fill='red', outline='yellow', tags='fruit')
        pass
    
    def get_oval_points(self, position):
        grid= MainCanvasClass.grid_value
        points = [position[0]+(grid/2), position[1]+(grid/2), position[0]-(grid/2), position[1]-(grid/2)]
        return points

    @classmethod
    def new_location(cls):
        frame = MainCanvasClass.get_framesize()
        cls.fruit_location = [randint(1, (frame[0]-10)/10)*10, randint(1, (frame[1]-10)/10)*10]
        return

class MainCanvasClass():
    grid_value = 10
    framesize = [1200, 800]
    game_status = 1
    eating_status = 0
    head_position = [framesize[0]/2, framesize[1]/2]
    direction = [0, 0]
    last_direction = [0, 0]
    snake_length=1
    snake_info=[]
    
    def __init__(self, root):
        self.fruit_location = self.randomfruit_point()
        self.root = root
        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1) 
        self.canvas = Canvas(self.canvas_frame, width=self.framesize[0]/2, height=self.framesize[0]/2)
        self.border = self.canvas.create_rectangle(0,0,self.framesize[0],self.framesize[1], fill='', outline='green', width=9, tags=('border'))
        self.snakeclass = Snake(self.canvas, self.grid_value)
        self.fruit = Fruit(self.canvas)
        self.startframe = StartFrame(self.canvas)
        
        
    def make(self):
        self.canvas.config(width=self.framesize[0], height=self.framesize[1], bg='black')
        self.canvas.grid(column=0, row=0, sticky='nswe')
        self.canvas.create_window(10, 10, anchor='nw', window=self.startframe.make(), tags=('startframe'))
        self.fruit.make()
        self.snakeclass.start()
        self.canvas.bind("<Return>", lambda e: maincanvas.game(e))     
        self.canvas.bind("<Up>", lambda e: self.snakeclass.keyup(e))     
        self.canvas.bind("<Left>", lambda e: self.snakeclass.keyleft(e))     
        self.canvas.bind("<Right>", lambda e: self.snakeclass.keyright(e))     
        self.canvas.bind("<Down>", lambda e: self.snakeclass.keydown(e))     
        return self.canvas_frame



    def game(self, event):
        if self.game_status == 1 :
            self.canvas.delete('startframe')
            self.game_status=2
            self.canvas.pack()
        self.move()
    
    def move(self):
        self.game_status = self.snakeclass.move()
        if self.game_status == 2:
            self.canvas.after(10, self.move)
        else:
            self.canvas.itemconfigure("head", fill='red', outline='red')
            self.canvas.itemconfigure("tail", fill='red', outline='red')
            self.canvas.itemconfigure("body", fill='red', outline='red')

    def get_canvas(self):
        return self.canvas

    def randomfruit_point(self):
        pos = [(randint(1, (self.framesize[0]-self.grid_value)/self.grid_value))*self.grid_value, (randint(1, (self.framesize[1]-self.grid_value)/self.grid_value))*self.grid_value ]
        return [pos[0]+(self.grid_value/2),pos[1]+(self.grid_value/2),pos[0]-(self.grid_value/2),pos[1]-(self.grid_value/2)] 

    def random_point(self):
        return [(randint(1, (self.framesize[0]-self.grid_value)/self.grid_value))*self.grid_value, (randint(1, (self.framesize[1]-self.grid_value)/self.grid_value))*self.grid_value ]

    @classmethod
    def get_framesize(cls):
        return cls.framesize

    
    
class StartFrame():
    def __init__ (self, canvas):
        self.canvas = canvas
        self.startframe = ttk.Frame(self.canvas)
        self.startlabel = ttk.Label(self.startframe, text="press enter to start")
    
    def make(self):
        self.startlabel.grid(column=0, row=0, sticky='nswe')
        return self.startframe
        

    def idle(self):
        pass





root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1) 
maincanvas = MainCanvasClass(root)

maincanvas.make().grid(column=0, row=0, sticky='nswe')
maincanvas.get_canvas().focus_set()
root.mainloop()


