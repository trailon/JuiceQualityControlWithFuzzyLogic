#kütüphane kurulumu 
import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import os
import win32api
#Triangular Membership Function
input_meyve = 1
input_su = 1
input_seker = 1
text1 ="X"
text2 ="X"
def trimf(x, abc):
    assert len(abc) == 3, 'abc parameter must have exactly three elements.'
    a, b, c = np.r_[abc]     # Zero-indexing in Python
    assert a <= b and b <= c, 'abc requires the three elements a <= b <= c.'

    y = np.zeros(len(x))

    # Left side
    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)

    # Right side
    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

    idx = np.nonzero(x == b)
    y[idx] = 1
    return y

#üyelik fonksiyonları
def main():
    #Genel tanım aralıkları
    x_meyve=np.arange(20,101,1)
    x_seker=np.arange(0,10,1)
    x_su=np.arange(0,81,1)
    x_kalite=np.arange(0,101,1)
    #Meyve miktar aralıkları
    meyve_low = trimf(x_meyve,[20,20,40])
    meyve_med = trimf(x_meyve,[35,53,70])
    meyve_high = trimf(x_meyve,[65,100,100])

    #Seker miktar aralıkları
    seker_low = trimf(x_seker,[0,0,3])
    seker_med = trimf(x_seker,[2,4,6])
    seker_high = trimf(x_seker,[5,9,9])

    #Su miktar aralıkları
    su_low = trimf(x_su,[0,0,25])
    su_med = trimf(x_su,[20,33,45])
    su_high = trimf(x_su,[40,80,80])

    #Kalite çıkış aralıkları
    kalite_az = trimf(x_kalite,[0,0,40])
    kalite_orta = trimf(x_kalite,[20,50,80])
    kalite_cok = trimf(x_kalite,[60,100,100])

    #Meyve çıkışları figür
    fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows = 4, figsize = (6,10))
    ax0.plot(x_meyve, meyve_low, 'r', linewidth = 2, label = 'Düşük')
    ax0.plot(x_meyve, meyve_med, 'g', linewidth = 2, label = 'Orta')
    ax0.plot(x_meyve, meyve_high, 'b', linewidth = 2, label = 'Yüksek')
    ax0.set_title('Meyve miktari')
    ax0.legend()

    #Seker çıkışları figür
    ax1.plot(x_seker, seker_low, 'r', linewidth = 2, label = 'Düşük')
    ax1.plot(x_seker, seker_med, 'g', linewidth = 2, label = 'Orta')
    ax1.plot(x_seker, seker_high, 'b', linewidth = 2, label = 'Yüksek')
    ax1.set_title('Seker miktari')
    ax1.legend()

    #Su çıkışları figür
    ax2.plot(x_su, su_low, 'r', linewidth = 2, label = 'Düşük')
    ax2.plot(x_su, su_med, 'g', linewidth = 2, label = 'Orta')
    ax2.plot(x_su, su_high, 'b', linewidth = 2, label = 'Yüksek')
    ax2.set_title('Su miktarı')
    ax2.legend()

    #Kalite çıkışları figür
    ax3.plot(x_kalite,kalite_az, 'r' , linewidth = 2, label = 'Düşük')
    ax3.plot(x_kalite,kalite_orta, 'g' , linewidth = 2, label = 'Orta')
    ax3.plot(x_kalite,kalite_cok, 'b' , linewidth = 2, label = 'Yüksek')
    ax3.set_title('Kalite çıkışı')
    ax3.legend()
    plt.tight_layout()
    
    #Meyve üyelik derecesi fonksiyonu
    meyve_fit_low = fuzzy.interp_membership(x_meyve, meyve_low, input_meyve)
    meyve_fit_med = fuzzy.interp_membership(x_meyve, meyve_med, input_meyve)
    meyve_fit_high = fuzzy.interp_membership(x_meyve, meyve_high, input_meyve)

    #Seker üyelik derecesi fonksiyonu
    seker_fit_low = fuzzy.interp_membership(x_seker, seker_low, input_seker)
    seker_fit_med = fuzzy.interp_membership(x_seker, seker_med, input_seker)
    seker_fit_high = fuzzy.interp_membership(x_seker, seker_high, input_seker)

    #Su üyelik derecesi fonksiyonu
    su_fit_low = fuzzy.interp_membership(x_su,su_low,input_su)
    su_fit_med = fuzzy.interp_membership(x_su,su_med,input_su)
    su_fit_high = fuzzy.interp_membership(x_su,su_high,input_su)

    #Kurallar
    rule1  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_low),seker_fit_low),kalite_az)
    rule2  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_low),seker_fit_med),kalite_az)
    rule3  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_low),seker_fit_high),kalite_az)
    rule4  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_med),seker_fit_low),kalite_az)
    rule5  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_med),seker_fit_med),kalite_az)
    rule6  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_med),seker_fit_high),kalite_az)
    rule7  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_high),seker_fit_low),kalite_az)
    rule8  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_high),seker_fit_med),kalite_az)
    rule9  = np.fmin(np.fmin(np.fmin(meyve_fit_low,su_fit_high),seker_fit_high),kalite_az)
    rule10 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_low),seker_fit_low),kalite_az)
    rule11 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_low),seker_fit_med),kalite_orta)
    rule12 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_low),seker_fit_high),kalite_orta)
    rule13 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_med),seker_fit_low),kalite_cok)
    rule14 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_med),seker_fit_med),kalite_cok)
    rule15 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_med),seker_fit_high),kalite_cok)
    rule16 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_high),seker_fit_low),kalite_orta)
    rule17 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_high),seker_fit_med),kalite_orta)
    rule18 = np.fmin(np.fmin(np.fmin(meyve_fit_med,su_fit_high),seker_fit_high),kalite_orta)
    rule19 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_low),seker_fit_low),kalite_cok)
    rule20 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_low),seker_fit_med),kalite_cok)
    rule21 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_low),seker_fit_high),kalite_cok)
    rule22 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_med),seker_fit_low),kalite_cok)
    rule23 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_med),seker_fit_med),kalite_cok)
    rule24 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_med),seker_fit_high),kalite_cok)
    rule25 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_high),seker_fit_low),kalite_az)
    rule26 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_high),seker_fit_med),kalite_az)
    rule27 = np.fmin(np.fmin(np.fmin(meyve_fit_high,su_fit_high),seker_fit_high),kalite_az)
    
    #Kuralların 'veya'lanarak kalite çıkışı için hazırlanması
    out_az = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax
    (np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax
    (np.fmax(rule1,rule27),rule26),rule25),rule2),rule3)
    ,rule4),rule5),rule6),rule7),rule8),rule9),rule10)
    out_orta = np.fmax(np.fmax(np.fmax(np.fmax
    (rule11,rule12),rule16),rule17),rule18)
    out_çok = np.fmax(np.fmax(np.fmax(np.fmax
    (np.fmax(np.fmax(np.fmax(np.fmax
    (rule24,rule23),rule13),rule14),rule15)
    ,rule19),rule20),rule21),rule22)

    #Kalite çıkış grafiğinin çizimi
    kalite0 = np.zeros_like(x_kalite)
    fig,ax0 = plt.subplots(figsize = (7,4))
    ax0.fill_between(x_kalite,kalite0,out_az,facecolor='r',alpha=0.7)
    ax0.plot(x_kalite,kalite_az,'r',linestyle='--')
    ax0.fill_between(x_kalite,kalite0,out_orta,facecolor='g',alpha=0.7)
    ax0.plot(x_kalite,kalite_orta,'g',linestyle='--')
    ax0.fill_between(x_kalite,kalite0,out_çok,facecolor='b',alpha=0.7)
    ax0.plot(x_kalite,kalite_cok,'b',linestyle='--')
    ax0.set_title('Kalite çıkışı')

    # Kalite çıkış değeri Durulaştırma işlemi ve
    # Durulaştırma çıkış değerinin grafik üyelik derecesi
    out_kalite = np.fmax(np.fmax(out_az,out_orta),out_çok)
    defuzzified = fuzzy.defuzz(x_kalite,out_kalite,'centroid')
    result = fuzzy.interp_membership(x_kalite,out_kalite,defuzzified)

    #GUI'de gösterilecek textin atanması
    global text1
    global text2
    text1 = "Durulastirma sonucu kalite cikisi yuzdesi = " , defuzzified
    text2 = "Durulasma degerinin grafige gore uyelik derecesi = " , result
    
#GUI
root = tk.Tk()
root.geometry("400x1000")

#GUI Metin bölgesinden girdi çeken fonksiyon
def degeral():
    global input_meyve
    global input_su
    global input_seker
    input_meyve = e1.get()
    input_su = e2.get()
    input_seker = e3.get()

    #Girdi kontrolü
    if(kontrol()):
        main()
        label1 = tk.Label(root,text=text1)
        label1.pack()
        label2 = tk.Label(root,text=text2)
        label2.pack()
        plt.show()

#Girdi kontrol fonksiyonu
def kontrol():
    if(int(e1.get())<20 or int(e2.get())>80 or int(e3.get())>9):
        win32api.MessageBox(0, 'Meyve 20den küçük Su 80den büyük Seker 9dan büyük olamaz', 'Hata')
        return False
    elif(int(e1.get())+int(e2.get())+int(e3.get()) >100):
        win32api.MessageBox(0, 'Meyve Su ve Seker yüzdelerinin toplamı 100ü geçemez', 'Hata')
        return False
    elif(int(e1.get())+int(e2.get())+int(e3.get()) <100):
        win32api.MessageBox(0, 'Meyve Su ve Seker yüzdelerinin toplamı 100ün altında olamaz', 'Hata')
        return False
    return True

#GUI materyalleri   
labelmeyve = tk.Label(root,text="Meyve")
labelmeyve.pack()
e1 = tk.Entry(root)
e1.pack()
labelsu = tk.Label(root,text="Su")
labelsu.pack()
e2 = tk.Entry(root)
e2.pack()
labelseker = tk.Label(root,text="Seker")
labelseker.pack()
e3 = tk.Entry(root)
e3.pack()
b=tk.Button(root,text="Degerleri al",command=degeral)
b.pack()
root.mainloop()