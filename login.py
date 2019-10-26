### ADD BUTTON REGARDING COUNTER.  2 is the last line in counter!
from tkinter import *
import os
import json
from selenium import webdriver
from getpass import getpass
from functools import partial


creds = 'tempfile.temp'# This just sets the variable creds to 'tempfile.temp'
store = 'storefile.json'
global lines#made lines global
global lines2
global editcounter
global editnum
global nye
global nyl
global nyk
nye="                                                                                                                                                         "
nyl="                                                                                                                                                "
nyk="                                                                                                                                                         "
editnum =0
editcounter =0
global listedit
listedit =[]
global linebutton
linebutton =1
global ld
ld = []
with open('storefile.json') as fii:
	lines =[line.rstrip('\n') for line in fii.readlines()]
with open('storefile.json') as fii:
	lines2 =[line.rstrip('\n') for line in fii.readlines()]
global linecount


#data = json.load(open("dat.json"))# This just sets the variable cstore to 'storefile.temp'


def Signup():  # This is the signup definition,
    global pwordE  # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
    global editB
    global deleteB
    # make button universal
    roots = Tk()  # This creates the window, just a blank one.
    roots.title('Signup')  # This renames the title of said window to 'signup'
    roots.geometry("700x700+550+100")
    canvasSign = Canvas(roots, width=700, height=700, bg="white")
    canvasSign.pack()
    img = PhotoImage(file="lock.png")
    # img =img.resize(100,100)
    canvasSign.create_image(350, 70, anchor=N, image=img)
    intruction = Label(roots,
                       text='Please Enter New Credidentials\n',font ='Helvetica 25 bold',fg="red")  # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.place(x=160,y=0)  # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    nameL = Label(roots, text='New Username: ',font ='Helvetica 14 bold',fg="#F8A51D")  # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ',font ='Helvetica 14 bold',fg="#F8A51D")  # ^^
    nameL.place(x=100,y=100)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.place(x=100,y=150)  # ^^

    nameE = Entry(roots)  # This now puts a text box waiting for input.
    pwordE = Entry(roots,
                   show='*')  # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.place(x=230,y=100)  # You know what this does now :D
    pwordE.place(x=230,y=150)  # ^^

    signupButton = Button(roots, text='Signup',
                          command=FSSignup)  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.place(x=440,y=125)
    roots.mainloop()  # This just makes the window keep open, we will destroy it soon


def FSSignup():
    with open(creds, 'w') as f:  # Creates a document using the variable we made at the top.
        f.write(
            nameE.get())  # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n')  # Splits the line so both variables are on different lines.
        f.write(pwordE.get())  # Same as nameE just with pword var
        f.close()  # Closes the file

    roots.destroy()  # This will destroy the signup window. :)
    Login()  # This will move us onto the login definition :D


def Login():
    global nameEL
    global pwordEL  # More globals :D
    global rootA

    rootA = Tk()  # This now makes a new window.
    rootA.title('Login')  # This makes the window title 'login'
    rootA.geometry("700x700+550+100")
    canvas = Canvas(rootA, width=700, height=700,bg="#03A9F4")
    canvas.pack()
    rootA.config(bg="#03A9F4")
    img = PhotoImage(file="lock.png")
    #img =img.resize(100,100)
    canvas.create_image(350, 70, anchor=N, image=img)
    intruction = Label(rootA, text='KeyPass Login\n',font ='Helvetica 25 bold',fg="#F8A51D",bg="#03A9F4") # More labels to tell us what they do
    intruction.place(x=249,y=10)# Blahdy Blah
    nameL = Label(rootA, text='Username ',bg="#03A9F4",fg="#F8A51D",font ='Helvetica 18')
    #nameL['bg'] = nameL.rootA['bg']# More labels
    pwordL = Label(rootA, text='Password ',bg="#03A9F4",fg="#F8A51D",font ='Helvetica 18')  # ^
    nameL.place(x=310, y=315)
    pwordL.place(x=310, y=380)

    nameEL = Entry(rootA)# The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.place(x=260, y=345)
    pwordEL.place(x=260, y=410)
    loginB = Button(rootA, text='Login',
                 command=CheckLogin)  # This makes the login button, which will go to the CheckLogin def.
    loginB.place(x= 330, y =510)
    rmuser = Button(rootA, text='Delete User', fg='red',
                    command=DelUser)  # This makes the deluser button. blah go to the deluser def.
    rmuser.place(x=312,y=530)
    rootA.mainloop()
#Adding screen
def addAccount():
    global accountWindow
    global webEn
    global nameEn
    global pwEn
    storageWindow.destroy()
    accountWindow =Tk()
    accountWindow.title("Account")
    accountWindow.geometry("700x700+550+100")
    canvasadd = Canvas(accountWindow, width=700, height=700, bg="#03A9F4")
    canvasadd.pack()
    img = PhotoImage(file="add.png")
    canvasadd.create_image(350, 70, anchor=N, image=img)

    label = Label(accountWindow,text ="Please fill out  the information bellow: ",font ='Helvetica 36 ',fg="#F8A51D",bg="#03A9F4")
    label.place(x=50,y=10)
    #Left Side: Stating website, username and password:
    webaccount = Label(accountWindow, text='Website: ',fg="#F8A51D",)
    nameaccount = Label(accountWindow, text='Username:',fg="#F8A51D")  # More labels
    pwordaccount = Label(accountWindow, text='Password: ',fg="#F8A51D")  # ^
    webaccount.place(x=230,y=160)
    nameaccount.place(x=230,y=200)
    pwordaccount.place(x=230,y=240)
    #Entry for website, username and password:
    webEn =Entry(accountWindow)
    nameEn =Entry(accountWindow)
    pwEn =Entry(accountWindow, show ='*')
    webEn.place(x= 330, y=160)
    nameEn.place(x= 330, y=200)
    pwEn.place(x= 330, y=240)
    saveB = Button(accountWindow, text='Save',fg="#03A9F4",command= lambda : save())
    saveB.place(x=330,y=300)
    accountWindow.mainloop()


#save button
def save():# function will save info in a  text file
    global lines
    global lines2
    with open(store, 'a') as fp:
        fp.write("Breakfrom1line000")#to tell myself it's the next line
        fp.write('\n')
        fp.write(webEn.get())
        fp.write('\n')
        fp.write(nameEn.get())
        fp.write('\n')
        fp.write(pwEn.get())
        fp.write('\n')
        fp.close()
    lines.append("Breakfrom1line000")
    lines.append(webEn.get())
    lines.append(nameEn.get())
    lines.append(pwEn.get())
    lines2.append("Breakfrom1line000")
    lines2.append(webEn.get())
    lines2.append(nameEn.get())
    lines2.append(pwEn.get())
    accountWindow.destroy()
    pageOne()



def pageOne():

    global storageWindow
    storageWindow = Tk()
    global editcounter
    global editnum
    global listedit
    global linebutton
    global deleteB
    storageWindow.title('Password Storage') # makes the title of window "Password Storage"
    storageWindow.geometry("700x700+550+100")
    storageWindow.config(bg="#03A9F4")
    lit =Label(storageWindow, text ="Your accounts:", font ='Helvetica 18 bold',fg="white",bg="#03A9F4")
    lit.grid(row =0, column = 0, sticky = W)
    Label(storageWindow, text ="_______________________________________________________________________________________________________________",fg="#F8A51D",bg="#03A9F4").grid()
    #row 2 available and onwards
    AddButton = Button(storageWindow, text='Add Account', command=lambda: addAccount())
    AddButton.grid(row =0, column = 0,sticky = E)
    #####For loop for adding
    h=1
    i=1
    linecount =2
    for line in lines:
        if line == "Breakfrom1line000":
            global editB
            counter = 0
            editnum = editnum+1
            listedit.append(editnum)
            editB = Button(storageWindow, text='Edit', command=partial(edit,i))
            editB.grid(row=linecount+1, column=0, sticky=E)
            ld.append(editB)
            linebutton = linebutton +1
            i = i+4
        if line != "Breakfrom1line000":
            if counter ==0:
                global deleteB
                Label(storageWindow, text="Website:"+nye,font="Helvetica 16 bold",fg="white",bg="#F8A51D" ).grid(row=linecount,column = 0, sticky =W)
                Label(storageWindow, text=line,font="Helvetica 14 bold",fg="white",bg="#F8A51D").grid(row=linecount,column = 0,sticky =N)
                deleteB=Button(storageWindow, text="Delete",command=partial(deleteCommand,i))
                deleteB.grid(row=linecount,column =0,sticky=E)
            elif counter ==1:
                Label(storageWindow, text="Username:"+nyl,font="Helvetica 16 bold",fg="white",bg="#F8A51D").grid(row=linecount, column=0, sticky=W)
                Label(storageWindow, text=line,font="Helvetica 16 bold",fg="white",bg="#F8A51D").grid(row=linecount,column = 0, sticky =N)

                #editB = Button(storageWindow, text='Edit' +str(editnum), command=lambda: edit(editnum))
                #editB.grid(row=linecount,column = 0, sticky =E)
            elif counter == 2:
                Label(storageWindow, text="Password:"+nyk,font="Helvetica 16 bold",fg="white",bg="#F8A51D").grid(row=linecount, column=0, sticky=W)
                Label(storageWindow, text=line,font="Helvetica 16 bold",fg="white",bg="#F8A51D").grid(row=linecount,column = 0, sticky = N)
                autologB = Button(storageWindow, text='Auto Login',bg="#03A9F4", command=partial(autoLogin,h))
                autologB.grid(row=linecount, column=0, sticky=E)
                linecount = linecount + 1
                h=h+4
                Label(storageWindow, text = "________________________________________________________________________________________________________________",fg="#F8A51D",bg="#03A9F4").grid(row=linecount,column = 0, sticky =W)# add line :D
            counter = counter + 1
            linecount = linecount +1
    #######################look at add button addAccount() --> save case
    print (editcounter)
    storageWindow.mainloop()

def edit(number):# Edit the username password or website
    global go
    go = number
    print(number)
    print(ld)
    global editWindow
    global webUp
    global nameUp
    global pwUp
    storageWindow.destroy()
    editWindow = Tk()
    editWindow.title("Edit")
    editWindow.geometry("700x700+550+100")
    editWindow.config(bg="white")
    img = PhotoImage(file="edit.png")
    canvasedit = Canvas(editWindow, width=700, height=700, bg="white")
    canvasedit.pack()
    canvasedit.create_image(350, 70, anchor=N, image=img)
    label = Label(editWindow, text="Please update the information bellow **",font="Helvetica 25 bold",fg="red")
    label.place(x=100,y=0)
    # Left Side: Stating website, username and password:
    webupdate = Label(editWindow, text='Website: ',font="Helvetica 18 ",fg="#03A9F4")
    nameupdate = Label(editWindow, text='Username: ',font="Helvetica 18 ",fg="#03A9F4")  # More labels
    pwordupdate = Label(editWindow, text='Password: ',font="Helvetica 18 ",fg="#03A9F4")  # ^
    webupdate.place(x=5, y=100)
    nameupdate.place(x=5, y=150)
    pwordupdate.place(x=5, y=200)
    # Entry for website, username and password:
    webUp = Entry(editWindow)
    nameUp = Entry(editWindow)
    pwUp = Entry(editWindow, show='*')
    webUp.place(x=100,y=100)
    nameUp.place(x=100,y=150)
    pwUp.place(x=100, y=200)
    saveB = Button(editWindow, text='Save', command=lambda: updateSave())
    saveB.place(x=90,y=250)
    editWindow.mainloop()

def deleteCommand(number):
    numbers=number-4
    print("Delete  "+str(numbers+3))
    with open('storefile.json', 'r') as file:
        # read a list of lines into data
        datas = file.readlines()
    datas[numbers]=""
    datas[numbers+1]=""
    datas[numbers +2]=""
    datas[numbers+3]=""
    lines[numbers]=""
    lines[numbers +1]=""
    lines[numbers +2]=""
    lines[numbers+3] = ""
    with open('storefile.json', 'w') as file:
        file.writelines(datas)
    file.close()
    storageWindow.mainloop()
    storageWindow.destroy()
    pageOne()



def updateSave():###FOR THE EDIT FUNCTION
    global const
    global go
    print("HI")
    with open('storefile.json', 'r') as file:
        # read a list of lines into data
        datas = file.readlines()
    datas[go]=webUp.get() +"\n"
    datas[go+1]=nameUp.get()+"\n"
    datas[go +2]=pwUp.get()+"\n"
    lines[go]=webUp.get()
    lines[go +1]=nameUp.get()
    lines[go +2]=pwUp.get()
    with open('storefile.json', 'w') as file:
        file.writelines(datas)
    file.close()
    editWindow.destroy()
    pageOne()

def autoLogin(number):
    nump1=number +1
    nump2= number +2
    jangweb =""
    usr =""
    pwd=""

    with open(store) as f9:
        for i, line in enumerate(f9):
            if i == number:
                jangweb = str(line)
    f9.close()

    with open(store) as f99:
        for i, line in enumerate(f99):
            if i == nump1:
                usr = line
    f99.close()

    with open(store) as f999:
        for i, line in enumerate(f999):
            if i == nump2:
                pwd = line
    f999.close()
    print(jangweb)
    print(usr)
    print(pwd)
    driver = webdriver.Chrome("/Users/cssi/Desktop/chromedriver")
    #get i line
    if jangweb == 'www.facebook.com\n':
        driver.get('https://'+jangweb+'/')
        username_box = driver.find_element_by_id('email')  # insepect element and find Id
        username_box.send_keys(usr)  # Put username
        password_box = driver.find_element_by_id('pass')  # insepect element and find Id
        password_box.send_keys(pwd)  # put Password
        login_btn = driver.find_element_by_id('u_0_3')  # insepect element and find Id
        login_btn.submit()
    elif jangweb == 'www.twitter.com\n':
        driver.get('https://' + jangweb + '/login')
        username_box = driver.find_element_by_class_name('js-username-field email-input js-initial-focus')  # insepect element and find Id
        username_box.send_keys(usr)  # Put username
        password_box = driver.find_element_by_class_name('js-password-field')  # insepect element and find Id
        password_box.send_keys(pwd)  # put Password
        login_btn = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium') #put button # insepect element and find Id
        login_btn.submit()
    else:
        driver.get('https://' + jangweb + '/')


def CheckLogin():
    with open(creds) as f:
        data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

    if nameEL.get() == uname and pwordEL.get() == pword:  # Checks to see if you entered the correct data.
         # Pack is like .grid(), just different
        rootA.destroy()# destroys RootA meaning the login window
        pageOne()

    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()


def DelUser():####remove everything from file
    os.remove(creds)  # Removes the file
    rootA.destroy()  # Destroys the login window
    Signup()  # And goes back to the start!"""

if os.path.isfile(creds):
    Login()
else:  # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
#Edit needs to show text that you already posted!
# for edit 123..for edit 1, 567.. edit 2, 9,10,11.. for edit3 13,14,15... 17,18,19, skip the 4
#can edit button name so it's button1, button5, button9, button13, button17, button21