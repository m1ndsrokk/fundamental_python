#tipe data skalar / sederhana
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

#tipe data list/ daftar / array
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
anak.append('Limo')
print(anak)

#sapa anak ke 2
print(f'Hai {anak[1]}')

#sapa semua anak
for a in anak:
    print(f'Hai {a}')

for a in range(0, len(anak)):
    print(f'Hai {anak[a]}')