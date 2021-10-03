from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from encrypt import Encrypt



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        width = 500
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.root.title("ABSENSI")

        img=Image.open("gambar/tengah.jpg")
        img=img.resize((500, 300), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_image=Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=500, height=300)

        title_lbl = Label(bg_image, text = "ABSENSI BERBASIS DATA WAJAH", font=("times", 20, "bold"), bg="purple", fg="yellow")
        title_lbl.place(x=0, y=20, width = 500, height= 35)

        b1=Button(bg_image, text="Enkripsi", command=self.encrypt, cursor="hand2", activebackground= "red", font=("times", 12), bg="white",fg="blue", width=10)
        b1.place(x=20, y=100)

        '''''
        b2 = Button(bg_image, text="Deteksi Wajah", cursor="hand2",command=self.face_data, activebackground="red", font=("times", 12), bg="white",
                    fg="blue", width=10)
        b2.place(x=150, y=100)

        b3 = Button(bg_image, text="Kehadiran", cursor="hand2",command=self.hadir, activebackground="red", font=("times", 12), bg="white",
                    fg="blue", width=10)
        b3.place(x=300, y=100)

        b5 = Button(bg_image, text="Train Wajah",command=self.train_data, cursor="hand2", activebackground="red", font=("times", 12), bg="white",
                    fg="blue", width=10)
        b5.place(x=20, y=200)

        b1 = Button(bg_image, text="Foto", cursor="hand2",command=self.open_img, activebackground="red", font=("times", 12), bg="white",
                    fg="blue", width=10)
        b1.place(x=150, y=200)

        b1 = Button(bg_image, text="Keluar", cursor="hand2",command=root.destroy, activebackground="red", font=("times", 12), bg="white",
                    fg="blue", width=10)
        b1.place(x=300, y=200)
'''''


        #f_lbl = Label(self.root, image=self.photoimg)
        #f_lbl.place(x=0, y=0, width=1000, height=500)

    def encrypt(self):
        self.new_window=Toplevel(self.root)
        self.app=Encrypt(self.new_window)







if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()