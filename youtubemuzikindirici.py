from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.title('Youtube Müzik İndirici')
root.iconbitmap("C:\\Users\\omerselim\\Desktop\\youtubemuzikindirici\\indir.ico")

canvas1 = tk.Canvas(root, width = 300, height = 200, bg="gray")
canvas1.pack()

labelBaslik = tk.Label(text='Youtube Müzik İndirici', font="Courier")
canvas1.create_window(150, 40, window=labelBaslik)

entry1 = tk.Entry(root, width=40, bd=5)
entry1.insert(0, "Youtube Linki")
canvas1.create_window(150, 100, window=entry1)

def download():
    link = entry1.get()
    yt = YouTube(link)

    ys = yt.streams.get_audio_only()
    ys.download()
    messagebox.showinfo(title="Başarılı", message="İndirme İşlemi Tamamlandı")

button1 = tk.Button(text='İndir', command=download, bg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()