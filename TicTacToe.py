import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.title("Tic-Tac-Toe")
bclick=True
def tictactoe(buttons):
        global bclick
        if buttons["text"] == "" and bclick == True:
            buttons["text"] = "X"
            bclick = False
        elif buttons["text"] == "" and bclick == False:
            buttons["text"] = "O"
            bclick = True

        elif (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
              button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
              button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
              button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
              button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
              button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
              button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
              button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
                tkinter.messagebox.showinfo("WINNER X", "PLAYER 1 WON THE GAME")
        else:
                tkinter.messagebox.showinfo("WINNER O", "PLAYER O WON THE GAME")

buttons =tkinter.StringVar()
button1=tkinter.Button(root,text="",font=('Arial',20),command=lambda :tictactoe(button1))
button1.grid(row=1,column=0,sticky='snew')
button2 = tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button2))
button2.grid(row=1, column=1, sticky='snew')
button3 =tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button3))
button3.grid(row=1, column=2, sticky='snew')
button4 = tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button4))
button4.grid(row=2, column=0, sticky='snew')
button5 =tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button5))
button5.grid(row=2, column=1, sticky='snew')
button6 =tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8,command=lambda: tictactoe(button6))
button6.grid(row=2, column=2, sticky='snew')
button7 =tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button7))
button7.grid(row=3, column=0, sticky='snew')
button8 =tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button8))
button8.grid(row=3, column=1, sticky='snew')
button9 =tkinter.Button(root, text="", font=('Arial', 20),height=4,width=8, command=lambda: tictactoe(button9))
button9.grid(row=3, column=2, sticky='snew')
root.mainloop()