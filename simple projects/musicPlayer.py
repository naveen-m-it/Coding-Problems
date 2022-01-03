#Naveen M
from tkinter import ttk
from tkinter.constants import HORIZONTAL
import os
import tkinter as tk
from pygame import mixer
from tkinter import filedialog
import time
from mutagen.mp3 import MP3

class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
#-----------------------------------------------------------------------------------------
        self.list = []
        self.pos = 0
        self.isPlaying = False
        self.mark = 0
        self.file_path = r"./Music"
#------------------------------------------------------------------------------------------
        # Gui properties
        self.title("Music Player")
        self.geometry("600x400")
        # self.resizable(width=False,height=False)
        self.open_dir()
#-------------------------------------------------------------------------------------------
    def button_align(self):    
        self.play_btn = tk.Button(self,text="Play",command=self.music_play)
        self.play_btn.grid(row=self.i,column=0)
        self.pause_btn = tk.Button(self,text="Pause",command=self.music_pause)
        self.pause_btn.grid(row=self.i,column=1)
        self.next = tk.Button(self,text="Next",command=self.music_next)
        self.next.grid(row=self.i,column=3)
        self.prev = tk.Button(self,text="Back",command=self.music_prev)
        self.prev.grid(row=self.i,column=2)
        self.select_folder = tk.Button(self,text="Select",command=self.file_open)
        self.select_folder.grid(row=self.i,column=4)
        self.play_mark = tk.Label(self,text='<-')
        self.play_mark.grid(column=1)
        self.slide_btn = ttk.Scale(self,from_=0,to=100,value=0,orient=HORIZONTAL,length=400)
        self.slide_btn.grid(row=self.i+1,column=0,columnspan=5)
        self.time_label = ttk.Label(self,text='00:00:00/00:00:00')
        self.time_label.grid(row=self.i+1,column=6)
        self.i+=1
#------------------------------------------------------------------------------------------
    
#------------------------------------------------------------------------------------------
    def file_open(self):
        self.time_label.destroy()
        self.slide_btn.destroy()
        self.list.clear()
        self.play_btn.destroy()
        self.pause_btn.destroy()
        self.next.destroy()
        self.play_mark.destroy()
        self.select_folder.destroy()
        self.file_path = filedialog.askdirectory()
        self.open_dir()
#-------------------------------------------------------------------------------------------
    def open_dir(self):
        if self.file_path==None:    
            self.file_path = filedialog.askdirectory()
        self.openFile()
        self.pos = 0
        self.i=0
        for row in self.list:
            s = row[:10]
            self.t=tk.Label(self,text=s)
            self.t.grid(row=self.i,column=0)
            self.i+=1
        self.button_align()
#-------------------------------------------------------------------------------------------
    def openFile(self):
        self.list = []
        arr = os.listdir(f"{self.file_path}")
        for a in arr:
            if a.endswith(".mp3"):
                self.list.append(a)
#------------------------------------------------------------------------------------------
    def music_play(self):
        time.sleep(1)
        file = self.file_path+"/"+self.list[self.pos]
        self.play_mark.grid(row=self.mark)
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        self.slide_btn['value']=0
        self.find_len()
        self.time_label.after(1000,self.find_len)
        self.isPlaying = True
#-----------------------------------------------------------------------------------------
    def music_pause(self):
        if self.isPlaying:
            mixer.music.pause()
            self.isPlaying = False
        else:
            mixer.music.unpause()
            self.isPlaying = True
#-----------------------------------------------------------------------------------------
    def music_next(self):
        time.sleep(1)
        self.mark+=1
        self.pos+=1
        if self.pos>len(self.list)-1:
            self.pos=0
            self.mark=0
        file = self.file_path+"/"+self.list[self.pos]
        self.play_mark.grid(row=self.mark)
        if self.isPlaying:
            mixer.music.stop()
        mixer.music.load(file)
        self.slide_btn['value']=0
        mixer.music.play()
        self.find_len()
        self.isPlaying==True
#--------------------------------------------------------------------------------------------
    def music_prev(self):
        time.sleep(1)
        if self.isPlaying:
            mixer.music.stop()
            self.isPlaying = False
        if self.pos==0:
            self.pos=len(self.list)-1
            self.mark=len(self.list)-1
        else:
            self.pos-=1
            self.mark-=1
        file = self.file_path+"/"+self.list[self.pos]
        self.play_mark.grid(row=self.mark)
        if self.isPlaying:
            mixer.music.stop()
        mixer.music.load(file)
        self.slide_btn['value']=0
        mixer.music.play()
        self.find_len()
        self.isPlaying==True
#---------------------------------------------------------------------------------------------
    def find_len(self):
        song = MP3(self.file_path+"/"+self.list[self.pos])
        to = song.info.length
        tt = time.strftime("%H:%M:%S",time.gmtime(to))
        current_time = mixer.music.get_pos()/1000
        t = time.strftime("%H:%M:%S",time.gmtime(current_time))
        self.time_label['text']=str(t)+'/'+str(tt)
        self.slide_btn['value'] = (current_time/to)*100
        if str(t) == "23:59:59":
            self.music_next()
        self.time_label.after(100,self.find_len)

#--------------------------------------------------------------------------------------------
# Main method
if __name__ == "__main__":
    app = App()
    app.mainloop()
