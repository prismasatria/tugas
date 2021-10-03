from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import time
import datetime
import random



class Encrypt:
    def __init__(self, root):
        self.root = root
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        width = 500
        height = 250
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.root.title("Encrypt, Decrypt, Encode")

        img = Image.open("gambar/LandWater11.jpg")
        img = img.resize((500, 250), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=500, height=250)
        localtime = time.asctime(time.localtime(time.time()))

        title_lbl = Label(bg_image, text="Encrypt & Decrypt", font=("times", 10, "bold"), bg="blue",
                          fg="white")
        title_lbl.place(x=0, y=20, width=500, height=20)

        lblInfo = Label(bg_image, font=('arial', 10, 'bold'),
                        text=localtime, fg="Blue")
        lblInfo.place(x=150, y=5, width=200, height=10)



        Pesan = StringVar()
        key = StringVar()
        mode = StringVar()
        Hasil = StringVar()

        # fungsi keluar
        def qExit():
            root.destroy()

        # fungsi reset
        def Reset():

            Pesan.set("")
            key.set("")
            mode.set("")
            Hasil.set("")

        # labels
        lblMsg = Label(root, font=('arial', 10, 'bold'),
                       text="Masukkan Teks")
        lblMsg.place(x=10, y=70, width=100, height=20)

        txtMsg = Entry(root, font=('arial', 10, 'bold'),
                       textvariable=Pesan)
        txtMsg.place(x=200, y=70, width=200, height=20)

        lblkey = Label(root, font=('arial', 10, 'bold'),
                       text="kunci")
        lblkey.place(x=10, y=100, width=100, height=20)

        txtkey = Entry(root, font=('arial', 10, 'bold'),
                       textvariable=key)
        txtkey.place(x=200, y=100, width=200, height=20)

        lblmode = Label(root, font=('arial', 7, 'bold'),
                        text="masukkan E/D (Encrypt/Decrypt)")
        lblmode.place(x=10, y=140, width=150, height=20)

        txtmode = Entry(root, font=('arial', 10, 'bold'),
                        textvariable=mode)
        txtmode.place(x=200, y=140, width=20, height=20)

        lblService = Label(root, font=('arial', 10, 'bold'),
                           text="Hasil")
        lblService.place(x=10, y=170, width=100, height=20)

        txtService = Entry(root, font=('arial', 10, 'bold'),
                           textvariable=Hasil)
        txtService.place(x=200, y=170, width=200, height=20)



        #cipher
        import base64

        # Fungsi encode
        def encode(key, clear):
            enc = []

            for i in range(len(clear)):
                key_c = key[i % len(key)]
                enc_c = chr((ord(clear[i]) +
                             ord(key_c)) % 256)

                enc.append(enc_c)

            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        # Fungsi decode
        def decode(key, enc):
            dec = []

            enc = base64.urlsafe_b64decode(enc).decode()
            for i in range(len(enc)):
                key_c = key[i % len(key)]
                dec_c = chr((256 + ord(enc[i]) -
                             ord(key_c)) % 256)

                dec.append(dec_c)
            return "".join(dec)

        def Ref():
            print("Pesan ", (Pesan.get()))

            clear = Pesan.get()
            k = key.get()
            m = mode.get()

            if (m == 'e'):
                Hasil.set(encode(k, clear))
            else:
                Hasil.set(decode(k, clear))

            # Tampilkan pesan

        btnTotal = Button(bg_image,text="Tampilkan pesan", bg="blue", fg="white",
                          command=Ref, width=12, cursor="hand2")
        btnTotal.place(x=20, y=200)

        # Reset button
        btnReset = Button(bg_image,text="Reset", bg="green",
                          command=Reset, width=10, cursor="hand2")
        btnReset.place(x=150, y=200)

        # Exit button
        btnExit = Button(bg_image,text="Exit", bg="red", fg="yellow",
                         command=qExit, width=10)
        btnExit.place(x=280, y=200)


if __name__ == "__main__":
    root=Tk()
    obj=Encrypt(root)
    root.mainloop()