'''
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = KEY VALUE PAIR
'''

kamus_ind_eng = {'anak': 'son', 'ayah': 'father', 'ibu': 'mother', 'istri': 'wife'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])

data_gojek = dict(tanggal='2020-7-12', driver_list=[{'nama': 'Eko', 'jarak': 10}, {'nama': 'Dwi', 'jarak': 100},
                                                    {'nama': 'Tri', 'jarak': 50}, {'nama': 'Dwi', 'jarak': 70}])

print(data_gojek)
print(f"Driver disekitar {data_gojek['driver_list']}")
print(f"Driver disekitar {data_gojek['driver_list'][0]}")
print(f"Driver disekitar {data_gojek['driver_list'][3]}")
print(f"jarak driver #1: {data_gojek['driver_list'][0]['jarak']}")