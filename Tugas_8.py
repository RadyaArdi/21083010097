from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
    if i % 2 == 0:
       print("%d Genap" %i, "-Punya ID proses", getpid())
    else:
       print("%d Ganjil" %i, "-Punya ID proses", getpid())
    sleep(1)

x = int(input("input :"))

print("Sekuensial")
sekuensial_awal = time()
for i in range(x):
    cetak(i+1)
sekuensial_akhir = time()

print("Multiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(x):
    p = Process(target=cetak, args=(i+1,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()

process_akhir = time()

print("Multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(1, x+1))
pool.close()

pool_akhir = time()

print("Waktu Eksekusi Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu Eksekusi Multiprocessing.process :", process_akhir - process_awal, "detik")
print("Waktu Eksekusi Multiprocessing.pool :", pool_akhir - pool_awal, "detik")

