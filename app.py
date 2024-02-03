import tkinter as tk
import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
from tkinter import ttk
from tkinter import filedialog
from tkinter import Text
import subprocess



def quitCMD():
    quit()

class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("Posting", "park", "light")
        self.image_path = ""

        self.textinputvar = tk.StringVar()
        self.textFrame = self.addLabelFrame("Your Post")
        self.textFrame.t = Text(self.textFrame.master,
                      highlightthickness = 0,
                      borderwidth=0,
                      blockcursor=True,
                      font=("Courier", 12),
                      wrap="word",
                      width=40, height=10)
        self.textFrame.t.grid(row=0, column=0, padx=10, pady=10)
        self.textFrame.t.bind("<KeyRelease>", self.textupdate)
        self.Button("Upload Image", self.upload_image)
        self.Button("Post", self.post)
        self.Button("Quit", quitCMD)
        self.run()

    def textupdate(self, event):
        print("Current text status:", self.textFrame.t.get("1.0", "end-1c"))
        self.textinputvar.set(self.textFrame.t.get("1.0", "end-1c"))

    def printCMD(self):
        print("Button clicked!")
        print(self.textinputvar.get())
        print(self.image_path)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")],
                                                     title="Select an image",
                                                     initialdir="~/img/")
    def post(self):
        message = self.textinputvar.get()
        masto_cli = ""
        twitter_cli = ""

        if not message:
            print("No message to post")
            return

        if self.image_path:
            masto_cli = f"toot post -m {self.image_path} \"{message}\""
            twitter_cli = "echo \"No support for images in api\""
        else:
            masto_cli = f"toot post \"{message}\""
            twitter_cli = f"~/.local/bin/x -t \"{message}\""

        subprocess.run(masto_cli, shell=True)
        subprocess.run(twitter_cli, shell=True)

        quit()

if __name__ == "__main__":
    App()
