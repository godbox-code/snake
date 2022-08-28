from random import randint
import tkinter as tk
from tkinter import font
from tkinter import ttk

#Version 1.1

class Snake():
    eating = False
    test1 = "green"
    game_status = 1
    new_direction = [1,0] 
    snakelist = [[100, 100, 1, 0], [80, 100, 1, 0]] # [head][tail]
    bodylist  = [[80, 100, 1, 0], [90, 100, 1, 0]]
    
    

    def __init__(self, canvas, score):
        self.canvas = canvas
        self.grid  = MainCanvasClass.grid_value
        self.fruit = Fruit(canvas)
        self.score = score
        
    def start_position (self):
        frame = MainCanvasClass.get_framesize()
        base_pos = [randint(5, (frame[0]/10)-5)*10, randint(5, (frame[1]/10)-5)*10]
        posible_dir = [[0,1],[0,-1],[1,0],[-1,0]]
        base_dir = posible_dir[randint(0, 3)]
        self.snakelist = [[base_pos[0], base_pos[1], base_dir[0], base_dir[1]], [base_pos[0]-(20*base_dir[0]), base_pos[1]-(20*base_dir[1]), base_dir[0], base_dir[1]]]
        self.bodylist = [[base_pos[0]-(20*base_dir[0]), base_pos[1]-(20*base_dir[1]), base_dir[0], base_dir[1]], [base_pos[0]-(10*base_dir[0]), base_pos[1]-(10*base_dir[1]), base_dir[0], base_dir[1]]]
        self.new_direction =[base_dir[0], base_dir[1]]
        return


    def start(self):
        self.game_status = 2
        self.canvas.delete("snake")
        self.start_position()
        self.canvas.create_rectangle(self.get_rec_points([self.snakelist[0][0], self.snakelist[0][1]]), fill='green', outline='green', tags=('head', 'snake')) 
        self.canvas.create_rectangle(self.get_rec_points([self.snakelist[1][0], self.snakelist[1][1]]), fill='green', outline='green', tags=('tail', 'snake'))
        for body in self.bodylist:
            self.canvas.create_rectangle(self.get_rec_points([body[0], body[1]]), fill=self.test1, outline=self.test1, tags=('body', 'snake'))
        
    def move(self):
        if self.eating == True:
            self.fruit.eat()
            if self.snakelist[0][0]%self.grid == 0 and self.snakelist[0][1]%self.grid == 0: 
                self.bodylist.append(self.snakelist[0][:])
                self.snakelist[1][2], self.snakelist[1][3] =  self.bodylist[0][2], self.bodylist[0][3]
                self.canvas.delete("body")
                for body in self.bodylist:
                    self.canvas.create_rectangle(self.get_rec_points([body[0], body[1]]), fill=self.test1, outline=self.test1, tags='body')
                self.snakelist[0][2], self.snakelist[0][3] = self.new_direction
                self.eating = False
                self.score.add_score(1)
                self.fruit.make()
            self.canvas.move('head', self.snakelist[0][2], self.snakelist[0][3])
        else:
            if self.snakelist[0][0]%self.grid == 0 and self.snakelist[0][1]%self.grid == 0: 
                self.bodylist.append(self.snakelist[0][:])
                self.bodylist.pop(0)
                self.snakelist[1][2], self.snakelist[1][3] =  self.bodylist[0][2], self.bodylist[0][3]
                self.canvas.delete("body")
                for body in self.bodylist:
                    self.canvas.create_rectangle(self.get_rec_points([body[0], body[1]]), fill=self.test1, outline=self.test1, tags='body')
                self.snakelist[0][2], self.snakelist[0][3] = self.new_direction
            self.canvas.move('head', self.snakelist[0][2], self.snakelist[0][3])
            self.canvas.move('tail', self.snakelist[1][2], self.snakelist[1][3])
            self.fruit_colision()
        self.position_update()
        self.dead()
        return self.dead()

    def dead(self):
        if self.snakelist[0][0] < 10 or self.snakelist[0][0] > MainCanvasClass.framesize[0]-10 or self.snakelist[0][1] < 10 or self.snakelist[0][1] > MainCanvasClass.framesize[1]-10:
            return 3 # hit wall --- dead
        if [self.snakelist[0][0], self.snakelist[0][1]] == [self.snakelist[1][0], self.snakelist[1][1]]:
            print([self.snakelist[0][0], self.snakelist[0][1]], [self.snakelist[1][0], self.snakelist[1][1]])
            return 3 # hit tail --- dead
        for bit in self.bodylist:
            if [self.snakelist[0][0], self.snakelist[0][1]] == [bit[0], bit[1]]:
                return 3 # hit body --- dead
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
    tick=0
    
    def __init__(self, canvas):
        self.canvas = canvas

    def eat(self):
        self.canvas.delete("fruit")
        grid= MainCanvasClass.grid_value
        self.canvas.create_oval(self.fruit_location[0]+(grid/2)+self.tick, self.fruit_location[1]+(grid/2)+self.tick, self.fruit_location[0]-(grid/2)-self.tick, self.fruit_location[1]-(grid/2)-self.tick, fill='', outline='red', tags='fruit')
        self.canvas.tag_lower('snake', 'fruit')
        self.tick += 10
        return
        


    def make(self):
        self.canvas.delete("fruit")
        self.new_location()
        self.canvas.create_oval(self.get_oval_points(self.fruit_location), fill='red', outline='yellow', tags='fruit')
        self.tick = 0
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
        self.canvas = tk.Canvas(self.canvas_frame, width=self.framesize[0]/2, height=self.framesize[0]/2)
        self.border = self.canvas.create_rectangle(0,0,self.framesize[0],self.framesize[1], fill='', outline='green', width=9, tags=('border'))
        self.score= Score(self.canvas)
        self.snakeclass = Snake(self.canvas, self.score)
        self.fruit = Fruit(self.canvas)
        self.startframe = StartFrame(self.canvas)
        self.gameover = GameOver(self.canvas, self.score)
        

        
        
    def make(self):
        self.canvas.config(width=self.framesize[0], height=self.framesize[1], bg='black')
        self.canvas.grid(column=0, row=0, sticky='nswe')
        self.fruit.make()
        self.startframe.make()
        self.snakeclass.start()
        self.canvas.bind("<Return>", lambda e: maincanvas.game(e))     
        self.canvas.bind("<Up>", lambda e: self.snakeclass.keyup(e))     
        self.canvas.bind("<Left>", lambda e: self.snakeclass.keyleft(e))     
        self.canvas.bind("<Right>", lambda e: self.snakeclass.keyright(e))     
        self.canvas.bind("<Down>", lambda e: self.snakeclass.keydown(e))
        self.score.generate_score()
        return self.canvas_frame



    def game(self, event):
        if self.game_status == 1 :
            self.canvas.delete('startframe')
            self.canvas.delete('gameoverframe')
            self.game_status=2
        elif self.game_status == 3:
            self.canvas.delete('gameoverframe')
            self.snakeclass.start()
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
            self.canvas.after(5, self.gameover.game_over())

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
        self.snakefont = font.Font(family="Meera", size=200, weight='bold')
        self.subfont = font.Font(family="Meera", size=40, weight='bold')
        self.canvas = canvas
        
    def make(self):
        frame = MainCanvasClass.get_framesize()
        self.canvas.create_text(frame[0]/2,frame[1]/2, font=self.snakefont, text="SNAKE", fill="green", tags='startframe')
        self.canvas.create_text(frame[0]/2,frame[1]/2+125, font=self.subfont, text="Press Enter To Start", fill="green", tags='startframe')
        return 

class GameOver():

    def __init__ (self, canvas, score):
        self.snakefont = font.Font(family="Meera", size=175, weight='bold')
        self.scorefont = font.Font(family="Meera", size=30, weight='bold')
        self.canvas = canvas
        self.score = score
        
    def game_over(self):
        scoretext =(f"Final Score {self.score.get_score()}")
        frame = MainCanvasClass.get_framesize()
        self.canvas.create_text(frame[0]/2,frame[1]/2, font=self.snakefont, text="GAME OVER", fill="green", tags='gameoverframe')
        self.canvas.create_text(frame[0]/2,frame[1]/2+125, font=self.scorefont, text="Press Enter To Start Again", fill="green", tags='gameoverframe')
        self.canvas.create_text(frame[0]/2,frame[1]/2+200, font=self.scorefont, text=scoretext, fill="green", tags='gameoverframe')
        
        return 

class Score():
    pass
    

    def __init__ (self, canvas):
        self.scorefont = font.Font(family="Meera", size=30, weight='bold')
        self.position=[MainCanvasClass.get_framesize()[0]-30,30]
        self.canvas = canvas
        self.score = 0
        
    def generate_score(self):
        self.canvas.create_text(self.position, font=self.scorefont, text=self.score, fill="#003300", tags='score', anchor=tk.NE)
        self.canvas.tag_lower('score', 'snake')
        return
    
    def add_score(self, speed_multiplier):
        self.score +=  10*speed_multiplier
        self.canvas.delete("score")
        self.canvas.create_text(self.position, font=self.scorefont, text=self.score, fill="#003300", tags='score', anchor=tk.NE)
        return
    def get_score(self):
        return self.score
    

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1) 
maincanvas = MainCanvasClass(root)

maincanvas.make().grid(column=0, row=0, sticky='nswe')
maincanvas.get_canvas().focus_set()
root.mainloop()


