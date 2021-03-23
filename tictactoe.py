import tkinter as tki
import tkinter.messagebox
root=tki.Tk()                       # creating a window with name root
root.title("Tic-Tac-Toe")           # giving window a title

player_a=tki.StringVar()
player_b=tki.StringVar()
p1=tki.StringVar()
p2=tki.StringVar()

player_1=tki.Entry(root, textvariable=p1,bd=5)
player_1.grid(row=1,column=1,columnspan=8)
player_2=tki.Entry(root, textvariable=p2,bd=5)
player_2.grid(row=2,column=1,columnspan=8)

bclick=True
flag=0
buttons=tki.StringVar()

def btn_click(buttons):
    global bclick, flag, player_1, player_2, player_a, player_b
    if(buttons['text']=='' and bclick==True):
       buttons['text']='X'
       print("Player 1 played")
       bclick=False
       player_b=p2.get()+" Wins!"
       player_a=p1.get()+" Wins!"
       check_for_win()
       flag+=1
    elif(buttons['text']=='' and bclick==False):
       buttons['text']='O'
       print("Player 2 played")
       bclick=True
       check_for_win()
       flag+=1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button is already pressed")


# disabling button after a game
def disablebutton():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    button4.configure(state="disabled")
    button5.configure(state="disabled")
    button6.configure(state="disabled")
    button7.configure(state="disabled")
    button8.configure(state="disabled")
    button9.configure(state="disabled")

# funtion to check who won a game
def check_for_win():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
       button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
       button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
       button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
       button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
       button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
       button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
       button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" ):
        disablebutton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player_a)
    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
       button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
       button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
       button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
       button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
       button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
       button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
       button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" ):
        disablebutton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player_b)
    elif flag==8:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie!")
        
       
    
    
label=tki.Label(root,text="Player 1: ", bg="white",fg="black",font="Times 20 bold",height=1,width=8)
label.grid(row=1,column=0)
label=tki.Label(root,text="Player 2: ", bg="white",fg="black",font="Times 20 bold",height=1,width=8)
label.grid(row=2,column=0)

# giving button texts and functionality
button1=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button1))
button1.grid(row=3,column=0)
button2=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button2))
button2.grid(row=3,column=1)
button3=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button3))
button3.grid(row=3,column=2)
button4=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button4))
button4.grid(row=4,column=0)
button5=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button5))
button5.grid(row=4,column=1)
button6=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button6))
button6.grid(row=4,column=2)
button7=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button7))
button7.grid(row=5,column=0)
button8=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button8))
button8.grid(row=5,column=1)
button9=tki.Button(root, text="",fg="green",bg="grey",font="Times 20 bold",height=4,width=8,command=lambda:btn_click(button9))
button9.grid(row=5,column=2)

root.mainloop()
