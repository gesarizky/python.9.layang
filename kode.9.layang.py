# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com


# Menginput diagonal dan sisi
diago1 = float(input('Tulis Diagonal 1 Trapesium: '))
diago2 = float(input('Tulis Diagonal 2 Trapesium: '))
sisi1 = float(input('Tulis Sisi 1 Trapesium: '))
sisi2 = float(input('Tulis Sisi 2 Trapesium: '))

# Hitung Luas dan Keliling layang-layang
luas = (diago1 * diago2) / 2 
keliling = (sisi1 + sisi2)*2

#Menampilkan Hasil Perhitungan
print('Luas Layang-layang  adalah %0.2f' %luas)
print('keliling Layang-layang adalah %0.2f' %keliling)
