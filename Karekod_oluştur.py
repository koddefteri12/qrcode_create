from qrcode import *
import tkinter as tk
from tkinter import filedialog
from datetime import  *
import os
import sqlite3 as sql

#Tarih
bugün = date.today()

#FonksEkran ayarı fonksiyonları
def tam_ekran():
    root.attributes('-fullscreen', True)

def ekran_ayarla(parametre):
    root.geometry(parametre)

#Karekod oluşturma fonksiyonu
def karekod_olustur():
    link = link_entry.get()
    dosya_ismi = dosya_ismi_entry.get()
    kaydet_yeri = kaydedilecek_yer_var.get()
    if kaydet_yeri == "Klasör seçilmedi":
        print("Lütfen kayıt klasörünü seçiniz.")
        return
    img = make(link)
    tam_yol = os.path.join(kaydet_yeri, f"{dosya_ismi}.png")
    img.save(tam_yol)
    root2 = tk.Toplevel()
    root2.geometry("300x100+700+300")
    root2.title("Başarılı")
    root2.configure(bg="#d1fae5")
    başarı_label = tk.Label(root2, text="Karekod başarıyla kaydedildi!", fg="#065f46", bg="#d1fae5", font=("Arial", 12))
    başarı_label.pack(padx=20, pady=20)


# Kayıt klasörü seçme fonksiyonu
def kaydet_yeri_sec():
    path = filedialog.askdirectory(initialdir=os.getcwd(), title="Kayıt klasörü seç")
    if path:
        try:
            kaydedilecek_yer_var.set(path)
        except NameError:
            pass


#Giriş
root = tk.Tk()

#Başlık
root.title("QRcode create")

#Boyut ve arka plan
ekran_ayarla("700x500+550+150")
root.maxsize(700,500)
root.minsize(700,500)
root.configure(bg="#ffe4b5")

#Version ve tarih
version = "v0.0.1"
version_label=tk.Label(root,text="v0.0.1",fg="#000000",bg="#ffe4b5").place(x=650,y=470)
tarih = tk.Label(root,text=bugün,fg="#000000",bg="#ffe4b5").place(x=10,y=470)

#sayfa düzenlemesi
başlık_label = tk.Label(root,text="QRcode create",fg="#8b4513",bg="#ffe4b5",font=("Arial",20,"bold")).place(x=220,y=30)

link_label = tk.Label(root,text="Link veya kısa metin giriniz",fg="#8b4513",bg="#ffe4b5",font=("Arial",12)).place(x=250,y=100)
link_entry = tk.Entry(root,width=25,bg="#fff8dc",fg="#000000",font=("Arial",12))
link_entry.place(x=230,y=125)

# Kayıt yeri seçme alanı (buton + gösterge)
kaydedilecek_yer_var = tk.StringVar(value="Klasör seçilmedi")
kaydedilecek_yer_label = tk.Label(root, textvariable=kaydedilecek_yer_var, fg="#8b4513", bg="#ffe4b5", font=("Arial",12))
kaydedilecek_yer_label.place(x=150,y=175,width=400)
kaydet_button = tk.Button(root, text="Klasör Seç", command=kaydet_yeri_sec, bg="#8b4513", fg="white")
kaydet_button.place(x=300,y=205)

#Dosya ismi
dosya_ismi_label = tk.Label(root,text="Dosya ismi giriniz (uzantısız)",fg="#8b4513",bg="#ffe4b5",font=("Arial",12)).place(x=250,y=250)
dosya_ismi_entry = tk.Entry(root,width=25,bg="#fff8dc", fg="#000000",font=("Arial",12))
dosya_ismi_entry.place(x=230,y=275)

#Kaydet butonu
olustur_kaydet_button = tk.Button(root,text="Karekod Oluştur ve Kaydet",command=karekod_olustur,bg="#8b4513",fg="white",font=("Arial",12,"bold"))
olustur_kaydet_button.place(x=235,y=330)







root.mainloop()

