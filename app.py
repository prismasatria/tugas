from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from encrypt import Encrypt



class Menu:
    def __init__(self, root):
        self.root = root
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        width = 500
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.root.title("Menu")

        img=Image.open("gambar/tengah.jpg")
        img=img.resize((500, 300), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_image=Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=500, height=300)

        title_lbl = Label(bg_image, text = "Menu Enkripsi dan Generate", font=("times", 20, "bold"), bg="purple", fg="yellow")
        title_lbl.place(x=0, y=20, width = 500, height= 35)

        b1=Button(bg_image, text="Enkripsi", command=self.encrypt, cursor="hand2", activebackground= "red", font=("times", 12), bg="white",fg="blue", width=15)
        b1.place(x=180, y=180)


    def encrypt(self):
        self.new_window=Toplevel(self.root)
        self.app=Encrypt(self.new_window)







if __name__ == "__main__":
    root=Tk()
    obj=Menu(root)
    root.mainloop()