# Deklarasi matriks
matriks = []

# Meminta input pengguna untuk mengisi matriks 3x3:
print("Masukan elemen untuk matriks 3x3:")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukan elemen baris {1+1}, kolom {1+1}: "))
        baris.append(nilai)
        matriks.append(baris)
        
# Transpose matriks
transpose = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)
    
#Menampilkan
print("\nHasil transpose matriks:")
for baris in transpose:
    print(baris)