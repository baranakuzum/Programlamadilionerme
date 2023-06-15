from tkinter import *
from tkinter import messagebox

def hesapla():
    seviye = seviye_secim.get()
    sektor = sektor_secim.get()
    calisma_tercihi = calisma_tercihi_secim.get()
    ilgi_suresi = ilgi_suresi_secim.get()
    
    if not seviye or not sektor or not calisma_tercihi or not ilgi_suresi:
        messagebox.showerror("Hata", "Lütfen tüm seçenekleri işaretleyin.")
        return
    
    puan = 0
    
    if seviye == "a":
        puan += 1
    elif seviye == "b":
        puan += 2
    elif seviye == "c":
        puan += 3
    
    if sektor == "a":
        puan += 1
    elif sektor == "b":
        puan += 2
    elif sektor == "c":
        puan += 3
    
    if calisma_tercihi == "a":
        puan += 1
    elif calisma_tercihi == "b":
        puan += 2
    
    if ilgi_suresi == "a":
        puan += 1
    elif ilgi_suresi == "b":
        puan += 2
    elif ilgi_suresi == "c":
        puan += 3
    
    if puan <= 4:
        sonuc = "Önerilen programlama dilleri: HTML, CSS, JavaScript"
    elif puan <= 7:
        sonuc = "Önerilen programlama dili: Python"
    elif puan <= 11:
        sonuc = "Önerilen programlama dili: C#"
    
    messagebox.showinfo("Sonuç", sonuc)
    cevap = messagebox.askyesno("Yeniden Oynamak", "Yeniden oynamak ister misiniz?")
    if cevap:
        seviye_secim.set("")  
        sektor_secim.set("") 
        calisma_tercihi_secim.set("") 
        ilgi_suresi_secim.set("") 
        sonuc_label.config(text="") 
    else:
        pencere.destroy()

# Pencere oluşturma
pencere = Tk()
pencere.title("Yazılım Öneri Programı")

# Seviye seçimi
seviye_secim = StringVar()
seviye_label = Label(pencere, text="Çalışmak İstediğiniz Seviye:")
seviye_label.pack()
seviye_radio1 = Radiobutton(pencere, text="Kolay", variable=seviye_secim, value="a")
seviye_radio1.pack()
seviye_radio2 = Radiobutton(pencere, text="Orta", variable=seviye_secim, value="b")
seviye_radio2.pack()
seviye_radio3 = Radiobutton(pencere, text="Zor", variable=seviye_secim, value="c")
seviye_radio3.pack()

# Sektör seçimi
sektor_secim = StringVar()
sektor_label = Label(pencere, text="Yazılıma hangi sektörde gireceksiniz:")
sektor_label.pack()
sektor_radio1 = Radiobutton(pencere, text="Web", variable=sektor_secim, value="a")
sektor_radio1.pack()
sektor_radio2 = Radiobutton(pencere, text="Veri bilimi", variable=sektor_secim, value="b")
sektor_radio2.pack()
sektor_radio3 = Radiobutton(pencere, text="Oyun", variable=sektor_secim, value="c")
sektor_radio3.pack()

# Çalışma tercihi seçimi
calisma_tercihi_secim = StringVar()
calisma_tercihi_label = Label(pencere, text="Nasıl çalışmak istersiniz:")
calisma_tercihi_label.pack()
calisma_tercihi_radio1 = Radiobutton(pencere, text="Freelance", variable=calisma_tercihi_secim, value="a")
calisma_tercihi_radio1.pack()
calisma_tercihi_radio2 = Radiobutton(pencere, text="Kurumsal firma", variable=calisma_tercihi_secim, value="b")
calisma_tercihi_radio2.pack()

# İlgi süresi seçimi
ilgi_suresi_secim = StringVar()
ilgi_suresi_label = Label(pencere, text="Kod yazmaya ne kadar süredir ilgi duyuyorsunuz:")
ilgi_suresi_label.pack()
ilgi_suresi_radio1 = Radiobutton(pencere, text="Yeni", variable=ilgi_suresi_secim, value="a")
ilgi_suresi_radio1.pack()
ilgi_suresi_radio2 = Radiobutton(pencere, text="Birkaç aydır", variable=ilgi_suresi_secim, value="b")
ilgi_suresi_radio2.pack()
ilgi_suresi_radio3 = Radiobutton(pencere, text="Bir yıldan fazla", variable=ilgi_suresi_secim, value="c")
ilgi_suresi_radio3.pack()

# Hesapla düğmesi
hesapla_button = Button(pencere, text="Hesapla", command=hesapla)
hesapla_button.pack()

# Sonuç etiketi
sonuc_label = Label(pencere, text="")
sonuc_label.pack()

# Pencereyi açma
pencere.mainloop()
