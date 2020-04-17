#!/usr/bin/env python
# coding: utf-8

# # Tkinter Assignment

# In[4]:


#1)
from tkinter import *
#mainscreen = Tk()
def main_screen():    
    mainscreen = Tk()
    mainscreen.geometry("300x200") 
    mainscreen.title("iDeators") 
def sub_screen():       
    subscreen = Tk()
    subscreen.geometry("300x200")  
    subscreen.title("Register") 
    Label(subscreen,text="Please enter details below", width="30", height="2", font=("Calibri", 13)).pack() 
    label1=Label(subscreen,text="Username*")  
    label1.pack()
    Entry1 =Entry(subscreen, bd=3)
    Entry1.pack()
    label2=Label(subscreen,text="Password*")  
    label2.pack()
    Entry2 =Entry(subscreen, bd=3)
    Entry2.pack()

    button2 = Button(subscreen, text="Register")
    button2.pack()
    
Label(text="iDeators", bg="gray", width="30", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

Button(text="Login", height="2", width="30",command=sub_screen).pack() 

Button(text="Register", height="2",width="30").pack()

mainscreen.mainloop()
main_screen() 


# In[1]:


#2)
import tkinter as tk
from tkinter import font
import PIL.Image
import PIL.ImageTk
import requests

#API_KEY = 'INSERT API KEY' #TODO insert API key from Openweathermap.com

#functions
def test_function(entry):
    print("button clicked", entry)

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, description, temperature)
    except:
        final_str = 'There was a problem retrieving that information.'

    return final_str

def get_weather(city):
    #weather_key = API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather?appid=cbf40c31dc6e53a5b63069b956572b3a'
    params = {'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    format_response(weather)

    label['text'] = format_response(weather)

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

im = PIL.Image.open("sky.jpg")
photo = PIL.ImageTk.PhotoImage(im)
background_label = tk.Label(root, image=photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#87cefa", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", fg="white", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#90c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
 


# In[ ]:




