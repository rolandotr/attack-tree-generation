from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Generation of Attack Trees")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)
        self.master.geometry("800x500+100+100")
        self.label=Label(self, text = 'Select Specification File Here',font =('Verdana', 15))
        self.label.grid(row=1, column=0, sticky=W)


        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=2, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename(filetypes=(("Specification file", "*.mcrl2"),))
        if fname:
            try:
                os.system("FileParser.py "+fname)
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


if __name__ == "__main__":
    MyFrame().mainloop()