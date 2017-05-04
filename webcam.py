# Nama  : Alek Roigusta
# NIM   : 5301414038
# Prodi : Pendidikan Teknik Elektro, S1
# Makul : Pengolahan Citra DIgital

# Tugas memanggil webcam kemudian memberi efek brightness dan grayscale

import numpy as np # untuk mengambil deklarasi library numpy dan dipanggil dengan np
import cv2 # deklarasi untuk import library open cv

ambil = cv2.VideoCapture(0) # cv2.VideoCapture untuk memanggil kamera dan (0) menunjukkan kamera internal pada perangkat 

while(True):    # jika benar maka webcam akan terus berulang(kamera terus membuka)
    ret, webcam = ambil.read() # Mengambil gambar-gambar dari webcam
    cv2.imshow('webcam',webcam)   #Menampilkan hasil dari webcam yang telah diberi efek menjadi grayscale

    grayscale = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY) # untuk merubah hasil webcam yang berwarna(BGR) menjadi grayscale(hitam putih)
    cv2.imshow('abuabu',grayscale) #untuk menampilkan gambar grayscale pada jendela 'abuabu'
    
    brightness = cv2.addWeighted(webcam,1.5, np.zeros(webcam.shape, webcam.dtype), 0, 50) #untuk merubah hasil webcam yang berwarna(BGR) menjadi lebih cerah
    cv2.imshow('cerah',brightness) #untuk menampilkan gambar brightness pada jendela 'cerah'

    negatif = (255-grayscale) # untuk merubah hasil webcam yang berwarna(BGR) menjadi negatif
    cv2.imshow('kelis',negatif) #untuk menampilkan gambar negatif pada jendela 'kelis'

    if cv2.waitKey(1) & 0xFF == ord('q'):   # jika di tekan 'q' maka semua jendela yang menampilkan gambar hasil webcam akan ditutup
        break

cap.release()
cv2.destroyAllWindows()