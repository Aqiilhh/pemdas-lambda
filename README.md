# Penjelasan Kode Pengolahan Data Sampah

## Deskripsi
Program ini membaca data jumlah produksi sampah berdasarkan Kabupaten/Kota dari file Excel, kemudian melakukan beberapa analisis, seperti:
1. Menghitung total produksi sampah pada tahun tertentu.
2. Menghitung total produksi sampah per tahun.
3. Menghitung total produksi sampah per Kabupaten/Kota setiap tahun.
4. Mengekspor hasil analisis ke file **CSV** dan **Excel**.

## Struktur Program
1. **Input**: File Excel berisi data nama Kabupaten/Kota, jumlah produksi sampah, dan tahun.
2. **Proses**:
   - Membaca data menggunakan `pandas`.
   - Menghitung total sampah dengan iterasi (`iterrows`).
   - Menyimpan hasil dalam bentuk DataFrame.
   - Mengekspor hasil ke CSV dan Excel.
3. **Output**: 
   - File CSV dan Excel berisi total produksi sampah.
   - Video penjelasan kode.
   
## Video Penjelasan
Lihat penjelasan program melalui video berikut:
[![Penjelasan Program](https://youtu.be/t8t9dZHpKTE)

## Hasil File
Hasil yang dihasilkan oleh program:
- `total_produksi_sampah_per_tahun.csv`
- `total_produksi_sampah_per_kota_tahun.csv`
- `total_produksi_sampah_per_tahun.xlsx`
- `total_produksi_sampah_per_kota_tahun.xlsx`

---
