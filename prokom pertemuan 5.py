kelas =["Ali", "Budi", "Dinda","Caca", "Dinda","Elo"]

print('==================================================')

#proses
for i in range (0,len(kelas)):
#output yang berulang
    print('nama mahasiswa ke ', i+1, 'adalah', kelas[1])

#output
print(kelas[3])
print(kelas[1])
print(len(kelas))
print('=====================================================')




print("==============================")
#Matriks dengan ukuran 3 x 3

#input
matriksA =  [[1,2,3],
            [4,5,6],
            [7,8,9]]

#output
print(matriksA)

#format matrik ke 2
for x in range(0, len(matriksA)):
    print()
    for y in range (0, len(matriksA[0])):
        print (matriksA [x][y], end= '')
        print()

print('======================================')

