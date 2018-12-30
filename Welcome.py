import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import time
import webbrowser

def openlink():
    webbrowser.open("https://www.youtube.com")
def openTicTacToe():
    import TicTacToe

class ScreenTimeMonitor(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Take-A-Break Screen Time Monitor")
        self.title_font = tkfont.Font(family='Futura', size=20)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomePage,Prompt):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    def delayshow_frame(self,page_name):
        time.sleep(10)
        frame = self.frames[page_name]
        frame.tkraise()
class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background="gray")
        self.controller = controller
        label = tk.Label(self, text="Welcome!Do you wish to use the Take-A-Break Screen Time Monitor?", font=controller.title_font,background="gray")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Yes,please start.",
                            command=lambda: controller.delayshow_frame("Prompt"),highlightbackground="gray")
        button1.pack()



class Prompt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background="gray")
        self.controller = controller
        label = tk.Label(self, text="It's time to take a break!", font=controller.title_font,background="gray")
        label.pack(side="top", fill="x", pady=10)
        l1=tk.Label(self,text="Note: Clicking on close will stop the Screen Time Monitor",font='Futura',background="gray")
        l1.pack()
        button = tk.Button(self, text="Open YouTube",
                           command=lambda: openlink(),highlightbackground="gray")
        button.pack()
        button1=tk.Button(self,text="Play TicTacToe(2 players)",command=lambda:openTicTacToe(),highlightbackground="gray")
        button1.pack()
        button2 = tk.Button(self, text="Resume",
                           command=lambda: controller.delayshow_frame("Prompt"), highlightbackground="gray")
        button2.pack()

if __name__ == "__main__":
    app = ScreenTimeMonitor()
    app.mainloop()