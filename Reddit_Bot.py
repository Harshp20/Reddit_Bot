from tkinter import *
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common import exceptions
import getpass
from datetime import datetime
from selenium.webdriver.common.by import By

root= Tk()
upvotes = 0
root.title("RedditBot Live Vote Counter")
root.geometry("613x350+750+200")
root.resizable(False, False)

my_img= ImageTk.PhotoImage(Image.open('reddit-1920-800x450.png'))
label3= Label(root, image=my_img)
label3.place( relwidth=1, relheight=1.1)

root.iconbitmap('Icon2.ico') #ICON

class Reddit_Bot:

    def __init__(self):
        self.driver= webdriver.Chrome('chromedriver.exe')
        self.driver.execute_script("alert('Please check your Application console window for Log In. Please hit OK before continuing.')")
        self.username= str(input("\nEnter your username or email: "))
        self.password= getpass.getpass(prompt="(Hidden Password Entry): ")
        print('\nPlease Minimize This and Your Browser Window... Wait for the MAIN window to fetch Votes.\nATTENTION!! It will not respond until it fetches Votes. Thanks for your patience.')
        self.driver.get('https://old.reddit.com')
        time.sleep(4)
        
    
    def login(self):
        try:
            self.driver.find_element_by_xpath('//input[@name="user"]').send_keys(self.username)
        except Exception:
            self.driver.get('https://old.reddit.com')
            time.sleep(3)
            self.login()
        try:
            self.driver.find_element_by_xpath('//input[@name="passwd"]').send_keys(self.password)
        except Exception:
            self.driver.get('https://old.reddit.com')
            time.sleep(3)
            self.login()
        try:
            self.driver.find_element_by_xpath('//input[@name="passwd"]').send_keys(Keys.RETURN)
        except Exception:
            self.driver.get('https://old.reddit.com')
            time.sleep(3)
            self.login()
        time.sleep(4)
    

    def get_upvotes(self):            
            self.driver.get('https://old.reddit.com/user/{}/'.format(self.username))
            time.sleep(3)

            upvotes= self.driver.find_element_by_xpath('//div[@class="score likes"]').text
            unvoted= self.driver.find_element_by_xpath('//div[@class="score unvoted"]').text
            downvotes= self.driver.find_element_by_xpath('//div[@class="score dislikes"]').text

            if len(upvotes)>0:
                label1.config(text='Upvoted')
                label2.config(text=upvotes)
                label2.after(200, self.get_upvotes)
            
            elif len(unvoted)>0:
                label1.config(text='')
                label2.config(text='Unvoted')
                label2.after(200, self.get_upvotes)
            
            else:
                label1.config(text='Downvoted')
                label2.config(text=downvotes)
                label2.after(200, self.get_upvotes)



#Driver Code
label1= Label(root, text='Fetching votes...', font=("Helvetica", 20))
label1.place(relx=0.53, rely=0.128, anchor=CENTER)

label2= Label(root, text='', font=("Helvetica", 60))
label2.place(relx=0.53, rely=0.33, anchor=CENTER)

status_bar= Label(root, text='Declare Variables, Not War', bd=1.5, relief=SUNKEN, anchor=E)
status_bar.place(relx=0.5, rely=0.975, anchor=CENTER)

button1= Button(root, text='Quit', command= root.destroy)
button1.place(relx= 0.945, rely=0.925)

a= Reddit_Bot()
a.login()
a.get_upvotes()

root.mainloop()