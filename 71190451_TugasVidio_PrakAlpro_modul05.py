
'''
Buatlah sebuah program penghitung nilai Indeks Prestasi Semester (IPS). Input
bagi program:
• Jumlah mata kuliah
• Nilai A, B, C, dan D untuk setiap mata kuliah mahasiswa
Output program ialah hasil IPS yang didapatkan.
'''
jumlah_matkul=int(input('masukan jumlah mata kuliah:'))
nilai=0
total_nilai=0
for i in range (1,jumlah_matkul+1):
    print('nilai mata kuliah',i,':',end='')
    nilai=str(input())
    if nilai == 'A':
        total_nilai +=4
    elif nilai == 'B':
        total_nilai+=3
    elif nilai =='C':
        total_nilai +=2
    elif nilai =='D':
        total_nilai +=1
    else:
        total_nilai +=0
print('hasil ips= ',(total_nilai * 3/(jumlah_matkul*3)))