from collections import defaultdict
import tkinter as tk
from tkinter.ttk import *
from time import sleep
import sys
class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("475x550+50+50")
        self.ans = defaultdict(list)
        SIZE_X = 125
        SIZE_Y = 125
        self.s = True
        self.i = 0
        self.wm_attributes('-transparentcolor',"#ab23ff")
        self.resizable(width=False,height=False)
        self.title("Tic Tac Toe")
        self.color = 'green'
        # Lines
        self.line = tk.Canvas(self)
        self.line.create_line(2*SIZE_X-75,1*SIZE_Y-75,2*SIZE_X-75,4*SIZE_Y-75)
        self.line.create_line(3*SIZE_X-75,1*SIZE_Y-75,3*SIZE_X-75,4*SIZE_Y-75)
        self.line.create_line(1*SIZE_X-75,2*SIZE_Y-75,4*SIZE_X-75,2*SIZE_Y-75)
        self.line.create_line(1*SIZE_X-75,3*SIZE_Y-75,4*SIZE_X-75,3*SIZE_Y-75)
        self.line.create_line(0,475,500,475)
        self.line.pack(fill="both",expand=True)

        # inside Buttons
        self.btn_1 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="1":self.solve(t))
        self.btn_1.place(x=55,y=50)
        self.btn_1.config(borderwidth=0)
        self.btn_2 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="2":self.solve(t))
        self.btn_2.place(x=55+125,y=50)
        self.btn_2.config(borderwidth=0)
        self.btn_3 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="3":self.solve(t))
        self.btn_3.place(x=180+125,y=50)
        self.btn_3.config(borderwidth=0)
        self.btn_4 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="4":self.solve(t))
        self.btn_4.place(x=55,y=50+125+1)
        self.btn_4.config(borderwidth=0)
        self.btn_5 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="5":self.solve(t))
        self.btn_5.place(x=55+125,y=50+125+1)
        self.btn_5.config(borderwidth=0)
        self.btn_6 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="6":self.solve(t))
        self.btn_6.place(x=180+125,y=50+125+1)
        self.btn_6.config(borderwidth=0)
        self.btn_7 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="7":self.solve(t))
        self.btn_7.place(x=55,y=50+250+1)
        self.btn_7.config(borderwidth=0)
        self.btn_8 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="8":self.solve(t))
        self.btn_8.place(x=55+125,y=250+50+1)
        self.btn_8.config(borderwidth=0)
        self.btn_9 = tk.Button(self,text='',font='roboto 45',height=2//5,width=3,command=lambda t="9":self.solve(t))
        self.btn_9.place(x=180+125,y=50+250+1)
        self.btn_9.config(borderwidth=0)

        # buttons
        text = chr(int('0x27F3',16))
        self.reset_btn = tk.Button(self,text=text,font="roboto 20",borderwidth=0,command =self.reset,bg='green',fg='white')
        self.reset_btn.place(x=20,y=480)
        self.tit = tk.Label(self,text="Tic Tac Toe",font="roboto 20",fg='blue')
        self.tit.place(x=230,y=490)

        # theme
        self.theme = tk.Button(self,text="Theme",font="roboto 20",borderwidth=0,command=self.change_theme,background='orange',fg='white')
        self.theme.place(x=80,y=480)
    def change_theme(self):
        colors = ['red','blue','green','yellow','orange','black']
        self.btn_1['fg']=colors[self.i]
        self.btn_2['fg']=colors[self.i]
        self.btn_3['fg']=colors[self.i]
        self.btn_4['fg']=colors[self.i]
        self.btn_5['fg']=colors[self.i]
        self.btn_6['fg']=colors[self.i]
        self.btn_7['fg']=colors[self.i]
        self.btn_8['fg']=colors[self.i]
        self.btn_9['fg']=colors[self.i]
        self.i+=1
        if self.i>=len(colors):
            self.i=0
    # change line color
    def lines(self):
        self.color = 'red'
    # Winning window
    # text reset and reset dict
    def reset(self):
        self.btn_1['text']=''
        self.btn_2['text']=''
        self.btn_3['text']=''
        self.btn_4['text']=''
        self.btn_5['text']=''
        self.btn_6['text']=''
        self.btn_7['text']=''
        self.btn_8['text']=''
        self.btn_9['text']=''
        self.ans = defaultdict(list)
        self.s = True
    
    #  Put text on a Button
    def solve(self,t):
        if t=='1' and self.btn_1['text']=='':
            if self.s:
                self.btn_1.config(text="X")
                self.s=False
                self.btn_1['fg']='red'
                x = 'X'
            else:
                self.btn_1.config(text="O")
                self.s=True
                self.btn_1['fg'] = 'blue'
                x = 'O'
        elif t=='2' and self.btn_2['text']=='':
            if self.s:
                self.btn_2.config(text="X")
                self.btn_2['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_2.config(text="O")
                self.s=True
                self.btn_2['fg'] = 'blue'
                x = 'O'
        elif t=='3' and self.btn_3['text']=='':
            if self.s:
                self.btn_3.config(text="X")
                self.btn_3['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_3.config(text="O")
                self.s=True
                self.btn_3['fg'] = 'blue'
                x = 'O'
        elif t=='4' and self.btn_4['text']=='':
            if self.s:
                self.btn_4.config(text="X")
                self.btn_4['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_4.config(text="O")
                self.s=True
                self.btn_4['fg'] = 'blue'
                x = 'O'
        elif t=='5' and self.btn_5['text']=='':
            if self.s:
                self.btn_5.config(text="X")
                self.btn_5['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_5.config(text="O")
                self.s=True
                self.btn_5['fg'] = 'blue'
                x = 'O'
        elif t=='6' and self.btn_6['text']=='':
            if self.s:
                self.btn_6.config(text="X")
                self.btn_6['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_6.config(text="O")
                self.s=True
                self.btn_6['fg'] = 'blue'
                x = 'O'
        elif t=='7' and self.btn_7['text']=='':
            if self.s:
                self.btn_7.config(text="X")
                self.btn_7['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_7.config(text="O")
                self.s=True
                self.btn_7['fg'] = 'blue'
                x = 'O'
        elif t=='8' and self.btn_8['text']=='':
            if self.s:
                self.btn_8.config(text="X")
                self.btn_8['fg'] = 'red'
                self.s=False
                x = 'X'
            else:
                self.btn_8.config(text="O")
                self.btn_8['fg'] = 'blue'
                self.s=True
                x = 'O'
        elif t=='9' and self.btn_9['text']=='':
            if self.s:
                x = 'X'
                self.btn_9.config(text="X")
                self.btn_9['fg'] = 'red'
                self.s=False
            else:
                self.btn_9.config(text="O")
                self.btn_9['fg'] = 'blue'
                self.s=True
                x = 'O'
        sleep(.1)
        self.sample(t,x)
    def sample(self,t,x):
        sleep(.1)
        self.resolve(t,x)
    # check over or not
    
    def resolve(self,t,x):
        sleep(0.1)
        self.ans[x].append(int(t))
        count=0
        for i in [1,2,3]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            sleep(1)
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return
        count=0
        for i in [1,4,7]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return
        count=0
        for i in [1,5,9]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return
        count=0
        for i in [2,5,8]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return
        count=0
        for i in [4,5,6]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return
        count=0
        for i in [7,8,9]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return 
        count=0
        for i in [3,5,7]:
            for j in self.ans[x]:
                if i==j:
                    count+=1
        if count==3:
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()
            return
        print(x,self.ans[x])
        if len(self.ans['X'])+len(self.ans['O'])==9:
            sleep(.7)
            self.reset()
            self.withdraw()
            a = side()
            a.mainloop()

class side(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Tic Tac Toe")
        self.geometry("300x200")
        self.resizable(width=False,height=False)
        l = tk.Label(self,text="Game Over!",fg='blue',font='roboto 30')
        l.place(x = 50,y=10)
        text = chr(int('0x27F3',16))
        text_1 = chr(int('0x2715',16))
        e = tk.Button(self,text=text_1,font="roboto 30",command=self.exit,bg='red',fg='white')
        e.place(x = 160,y = 60)
        r = tk.Button(self,text=text,command=self.reset,font="roboto 30",bg='green',fg='white')
        r.place(x=50,y=60)
    def exit(self):
        sys.exit()
    def reset(self):
        self.destroy()
        App().deiconify()

if __name__ == "__main__":
    app = App()
    app.mainloop()