import sys
from tkinter import *
from selenium import webdriver

def GOURL():
    URL = ip.get()
    driver = webdriver.Chrome("directory of chromedriver\\chromedriver.exe")
    driver.get(URL)
    driver.maximize_window()
    fo = open("name_key.txt","r+")
    context = fo.read()
    context2 = context.split("\n")
    counter = len(context2)
    for i in range(0,counter,2):
        name = context2[i]
        key = context2[i+1]
        try:
            driver.find_element_by_name(name).send_keys(key)
        except:
            pass
        
# creating a window
mGui = Tk()
ip = StringVar()
mGui.geometry('450x450')
mGui.title('URL')
mlabel = Label(mGui,text = "Please insert URL").pack()
mEntry = Entry(mGui,width = 70,textvariable = ip).pack()
mbutton = Button(mGui , text = "OK",command = GOURL,fg = 'black',bg = 'grey').pack()
