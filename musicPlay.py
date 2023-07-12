
from tkinter import*
import pygame
from pygame import mixer 
from tkinter import filedialog
import os
root = Tk()
root.title ("telows media play") 
root.geometry("500x300")
root.config(bg="white")
mixer.init()
import time
from mutagen.mp3 import MP3







def add_song():
    song =filedialog.askopenfilename(initialdir="audio/",title="choose a song",filetypes=(("mp3 files","*.mp3"),))
    song_listbox.insert(END,song)
    song = song.replace("C:/audio/","")
    song=song.replace(".mp3","")


def play():
    song = song_listbox.get(ACTIVE)
    song = f'C:/audio/{song}.mp3'
    song=song.replace(".mp3","")
    mixer.music.load(song_listbox.get(ACTIVE))
    pygame.mixer.music.play()
    play_time()

    

def stop():
    pygame.mixer.music.stop()

global paused
paused=False
def pause():
    global paused
 
    if paused:
        pygame.mixer.music.unpause()
        puased=False
    else:
        pygame.mixer.music.pause()
        paused=True


def backward():
    backward=song_listbox.curselection()
    backward=backward[0]-1
    song=song_listbox.get(backward)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    song_listbox.selection_clear(0,END)
    song_listbox.activate(backward)
    song_listbox.selection_set(backward)

def forward():
    forward=song_listbox.curselection()
    forward=forward[0]+1
    song=song_listbox.get(forward)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    song_listbox.selection_clear(0,END)
    song_listbox.activate(forward)
    song_listbox.selection_set(forward)
 
def set_vol(val):
    volume= float(val) /200
    mixer.music.set_volume(volume)
muted = FALSE    

def play_time():
    current_time=pygame.mixer.music.get_pos()/1000
    converted_current_time =time.strftime('%M:%S',time.gmtime(current_time))

    song =song_listbox.get(ACTIVE)
    slider_bar.after(1000,play_time)
    song_mut =MP3(song)
    song_length = song_mut.info.length
    converted_song_length =time.strftime('%M:%S' , time.gmtime(song_length))
    slider_bar.config(text=f'Time Elapsed:{converted_current_time} of{converted_song_length}')
    
    
def scale():
    current_time=mixer.music.get_pos()/1000
    audio=MP3(song_listbox.get(ACTIVE))
    song_length=audio.info.length/60.0
    slider_pos=(current_pos_mins/song_length)*100
    slider_bar.set(slider_pos)
    root.after(100,scale)
    
            

song_listbox = Listbox(root, bg='pink',fg='white', width='60')
song_listbox.grid(pady=20)


forward_btn_img=PhotoImage(file=r"C:/Users/TRAINING2/Desktop/btn/forward.png")


backward_btn_img=PhotoImage(file=r"C:/Users/TRAINING2/Desktop/btn/backward.png")


play_btn_img=PhotoImage(file=r"C:/Users/TRAINING2/Desktop/btn/play.png")


pause_btn_img=PhotoImage(file=r"C:/Users/TRAINING2/Desktop/btn/pause.png") 


stop_btn_img=PhotoImage(file=r"C:/Users/TRAINING2/Desktop/btn/stop.png")

controls_frame=Frame(root)
controls_frame.grid()


forward_btn=Button(controls_frame,image=forward_btn_img,borderwidth=0,command=forward)
forward_btn.grid(column = 0,row=0,padx=10)

back_btn=Button(controls_frame,image=backward_btn_img,borderwidth=0,command=backward)
back_btn.grid(column = 1,row=0,padx=10)

play_btn=Button(controls_frame,image=play_btn_img,borderwidth=0,command=play)
play_btn.grid(column = 2,row=0,padx=10)

pause_btn=Button(controls_frame,image=pause_btn_img,borderwidth=0,command=pause)
pause_btn.grid(column = 3,row=0,padx=10)


stop_btn=Button(controls_frame,image=stop_btn_img,borderwidth=0,command=stop)
stop_btn.grid(column = 4,row=0 ,padx=10)


my_menu=Menu(root)
root.config(menu=my_menu)

add_song_menu=Menu(my_menu)
my_menu.add_cascade(label='add songs',menu=add_song_menu)
add_song_menu.add_command(label='add 1 song to playlist',command =add_song)

scale= Scale(controls_frame , from_=0, to =100, orient=VERTICAL,command=set_vol)
scale.set(5)
pygame.mixer.music.set_volume(0.05)
scale.grid(row=0, column=5, pady=50,padx=30)


scale= Scale(controls_frame , from_=0, to =100, orient=HORIZONTAL,command=scale)
scale.grid(row=1, column=6, pady=50,padx=30)



slider_bar=Label(root,text="",bd=1,relief=GROOVE,anchor=E,  )
slider_bar.grid(column=0,row=0,padx=30,pady=30)               
               
               




root.mainloop()
 
