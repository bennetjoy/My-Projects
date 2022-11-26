# import the GUI toolkit
# assigning sd variable as mainfunction
from tkinter import *
import tkinter.messagebox
# assigning sd variable as mainfunction
sd = Tk()
# sd.title() is used to show the title name as “TIC TAC TOE”.
sd.title("TIC TAC TOE")
# StringVar() is used to holds the string and it takes default as “”.
str1 = StringVar()
play = StringVar()
s1 = StringVar()
s2 = StringVar()
# it accepts single line string and entry from the user for Ticker_1.
Ticker_1 = Entry(sd, textvariable=s1, bd=5)
# grid method is used to arrange labels in rows and column as specified.
Ticker_1.grid(row=1, column=1, columnspan=8)
# similar to line 8 and 9 as it is for Ticker_2.
Ticker_2 = Entry(sd, textvariable=s2, bd=5)
Ticker_2.grid(row=2, column=1, columnspan=8)
# Intialising f to 0 and booly for True(i.e. 1)
booly = True;f = 0
# Defining function invisible for buttons to perform at intial condition.
def invisible():
# configuring from button 1 to 8 to be in disabled state.
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)
# Defining box selection function.
def boxselection(b):
# Declare global variables as booly, f, Ticker_1, Ticker_2,play, str1 so that it will run throughout the program executions or else it won’t work for full program.  
    global booly, f, Ticker_2, Ticker_1, play, str1
    #  If Boolean value is True and the text is ‘X’
    if b["text"] == " " and booly == True:
        b["text"] = "X"
        booly = False
# After satisfying anyone condition in Victory() function in if part it display as Ticker_2 wins orelse Ticker_1 wins.
        play = s2.get() + "Ticker 2 Wins!"
        str1 = s1.get() + "Ticker 1 Wins!"
# If Boolean value is False and the text is ’O’ and initialize Boolean value to True.
        Victory()
        f += 1
#After satisfying anyone condition in Victory() function in elif part it display as Ticker_2 wins orelse Ticker_1 wins.
    elif b["text"] == " " and booly == False:
        b["text"] = "O"
        booly = True
        Victory()
        f += 1
# else part describes about if button click is overridden then it shows message as(“Button already Clicked Please click other button”).
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked Please click other button")
#  Defining function as Victory, It consist as follow as,
def Victory():
# First all horizontal conditions are checking:
             # If button 1==2==3== ‘X’ or
                        #button 4==5==6==’X’ or
                        #button 7==8==9==’X’ or
                        #Diagonal conditions:
                        #button 1==5==9==’X’
                        #button 4==5==6==’X’
                        #Vertical conditions:
                        #button 1==4==7==’X’
                        #button 2==5==8==’X’
                        #button 3==6==9==’X’

    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
        b7['text'] =='X' and b8['text'] == 'X' and b9['text'] == 'X' or
        b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
        b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
        b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
        b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
        b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
# It will call invisible function if any of the conditions satisfied.
        invisible()
# It is used to show the message information.It goes to boxselection function(i.e.Line 24).
        tkinter.messagebox.showinfo("Tic-Tac-Toe", str1)
# If f==8 then it display the message as “It is a Tie” .
    elif(f == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
# It is similar to Line 41 to 49 the only difference is that instead of X here it is O,    
             #Horizontal Conditions,
                    #If button 1==2==3== ‘O’ or
                    #button 4==5==6==’O’ or
                    #button 7==8==9==’O’ or
                #Diagonal conditions:
                    #button 1==5==9==’O’
                    #button 4==5==6==’O’
                #Vertical conditions:
                    #button 1==4==7==’O’
                    #button 2==5==8==’O’
                    #button 3==6==9==’O’

    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
# It will call invisible function if any of the conditions satisfied.
# It is used to bold the String inside the boxes.
        invisible()
        tkinter.messagebox.showinfo("TIC-TAC-TOE", play)
# Label is a Tkinter widget class. It is used to display text and images. It contains
'''Name of the text(i.e. Ticker_1), font size is 15 bold ,
bg - The normal background color displayed behind the label and indicator.Here it is yellow colour.
fg - If you are displaying text or a bitmap in this label, this option specifies the color of the text.If you are displaying a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.Here it is darkgreen color. 
Height is 1 and width is 8.'''
b = StringVar()
# Using label method it will works in 1st row and 0th column by using grid.
label = Label( sd, text="Ticker 1:", font='Times 15 bold', bg='yellow', fg='darkgreen', height=1, width=8)
label.grid(row=1, column=0)

# It describes about button configurations with particular row and column as mentioned in Line 66 and 67 or 68 and 69.
label = Label( sd, text="Ticker 2:", font='Times 15 bold', bg='yellow', fg='darkgreen', height=1, width=8)
label.grid(row=2, column=0)

b1 = Button(sd, text=" ", font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b1))
b1.grid(row=3, column=0)

b2 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b2))
b2.grid(row=3, column=1)

b3 = Button(sd, text=' ',font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b3))
b3.grid(row=3, column=2)

b4 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b4))
b4.grid(row=4, column=0)

b5 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b5))
b5.grid(row=4, column=1)

b6 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b6))
b6.grid(row=4, column=2)

b7 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b7))
b7.grid(row=5, column=0)

b8 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b8))
b8.grid(row=5, column=1)

b9 = Button(sd, text=' ', font='Times 15 bold', bg='blue', fg='white', height=4, width=8, command=lambda: boxselection(b9))
b9.grid(row=5, column=2)
# Mainloop method is used to run the application, wait for an event to occur and process the event as long as it is not closed.
sd.mainloop()
