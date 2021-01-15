print ("\nPROGRAM PYTHON MENGHITUNG IPK MAHASISWA")

print ("\nBIODATA MAHASISWA")
nama = input ("Nama : ")
ttl = input ("Tempat Tanggal Lahir : ")
alamat = input ("Alamat : ")
jk = input ("Jenis Kelamin : ")
agama = input ("Agama : ")

print ("\nNILAI MATAKULIAH")
dm = int (input ("Nilai Data Maining : "))
pbw = int (input ("Nilai Pemrograman Berbasis Web : "))
sd = int (input ("Nilai Struktur Data : "))
rpl = int (input ("Nilai Rekayasa Perangkat Lunak : "))
ps = int (input ("Nilai Probabilistik dan Statistika : "))
mp = int (input ("Nilai Manajemen Proyek : "))

nilai = dm+pbw+sd+rpl+ps+mp;
jumlah_nilai = nilai/6;

if nilai >= 90 :
    print ("\nGrade = A")
elif nilai >= 85 :
    print ("\nGrade = B+")
elif nilai >= 75 :
    print ("\nGrade = B")
elif nilai >= 68 :
    print ("\nGrade = C+")
elif nilai >= 50 :
    print ("\nGrade = C")
elif nilai >= 35 :
    print ("\nGrade = D")
elif nilai <= 34 :
    print ("\nGrade = E")

print("Jumlah Nilai = ",float (jumlah_nilai))
if nilai >= 68 :
    print ("Kamu Lulus")
else :
    print ("Kamu Tidak Lulus")