import math

print("Program Menghitung Luas dan Volume Tabung")

#Programmer  : Ramdani Barkat Nugraha
#Pertemuan   : 1
#7Tanggal     : 22 Oktober 2023

#input nilai
jari_jari = 13
tinggi = 14

#rumus
luas_lingkaran = math.pi*jari_jari** 2
luas_selimut = 2 * math.pi*jari_jari * tinggi
luas = 2 * luas_lingkaran + luas_selimut
volume = luas_lingkaran*tinggi

#output
print(f"Luas: {luas}")
print(f"Volume: {volume}")