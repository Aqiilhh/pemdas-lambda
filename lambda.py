import pandas as pd

# Membaca data dari file Excel
file_path = 'disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx'
data = pd.read_excel(file_path)

# 1. Membuat DataFrame yang menyertakan nama Kabupaten/Kota, jumlah produksi sampah, dan tahun
df = data[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']]

# 2. Menghitung total produksi sampah di seluruh Kabupaten/Kota untuk tahun tertentu menggunakan iterrows
selected_year = 2015
total_sampah_tahun_tertentu = 0
for i, j in df.iterrows():
    if j['tahun'] == selected_year:
        total_sampah_tahun_tertentu += j['jumlah_produksi_sampah']
print(f"Total produksi sampah di Jawa Barat pada tahun {selected_year}: {total_sampah_tahun_tertentu} ton")

# 3. Menjumlahkan data per tahun menggunakan iterrows
total_tahunan = {}
for a, b in df.iterrows():
    tahun = b['tahun']
    total_tahunan[tahun] = total_tahunan.get(tahun, 0) + b['jumlah_produksi_sampah']

total_per_tahun_df = pd.DataFrame(list(total_tahunan.items()), columns=['Tahun', 'Total Produksi Sampah'])

# 4. Menjumlahkan data per Kota/Kabupaten per tahun menggunakan iterrows
total_tahunan_kota = {}

for x, y in df.iterrows():
    key = (y['nama_kabupaten_kota'], y['tahun'])
    total_tahunan_kota[key] = total_tahunan_kota.get(key, 0) + y['jumlah_produksi_sampah']

total_tahunan_kota_df = pd.DataFrame(
    [(key[0], key[1], value) for key, value in total_tahunan_kota.items()],
    columns=['Nama Kabupaten/Kota', 'Tahun', 'Total Produksi Sampah']
)

#eksport jadi file CSV
total_per_tahun_df.to_csv('total_produksi_sampah_per_tahun.csv', index=False)
total_tahunan_kota_df.to_csv('total_produksi_sampah_per_kota_tahun.csv', index=False)

#eksport menjadi file Excel
total_per_tahun_df.to_excel('total_produksi_sampah_per_tahun.xlsx', index=False)
total_tahunan_kota_df.to_excel('total_produksi_sampah_per_kota_tahun.xlsx', index=False)

print("Proses selesai. File CSV dan Excel telah dibuat.")
