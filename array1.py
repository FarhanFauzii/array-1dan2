angka = []

#Meminta input pengguna
for i in range(5):
    elemen = int(input(f"Masukan angka ke-{1+1}:"))
    angka.append(elemen)

# Mengurutkan angka dalam array
angka.sort()
    
# Menampilkan array yang sudah diurutkan
print(f"array yang sudah diurutkan: {angka}")     