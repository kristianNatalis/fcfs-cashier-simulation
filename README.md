
# 🛒 Simulasi Antrian Kasir Minimarket (Algoritma FCFS)

Program simulasi sederhana berbasis CLI (*Command Line Interface*) untuk memodelkan antrean kasir di minimarket menggunakan **Algoritma Penjadwalan FCFS (First Come First Serve)**. Proyek ini dibuat untuk memenuhi tugas mata kuliah *Computer Organization dan Operating Systems* dengan mengacu pada referensi buku *Operating Systems* oleh William Stallings.

---

## 📌 Anggota Tim / Identitas Mahasiswa
* **Nama:** Kristian Natalis
* **NIM:** 255314019
* **Prodi:** Informatika
* **Universitas:** Universitas Sanata Dharma, Yogyakarta

---

## 📖 Konsep & Rumus Perhitungan

Algoritma **FCFS (First Come First Serve)** menetapkan bahwa pelanggan yang datang lebih awal akan dilayani terlebih dahulu. Jika kasir sedang kosong dan pelanggan belum datang, kasir akan berada dalam kondisi *idle* (nganggur) hingga pelanggan berikutnya tiba.

Berikut adalah rumus-rumus utama yang digunakan dalam perhitungan simulasi ini:

| Komponen | Singkatan | Rumus | Arti |
| :--- | :---: | :--- | :--- |
| **Turnaround Time** | TAT | `Selesai - Datang` | Total waktu yang dihabiskan pelanggan dari datang sampai selesai belanja. |
| **Waiting Time** | WT | `TAT - Lama Layanan` | Waktu tunggu pelanggan di dalam antrean sebelum dilayani oleh kasir. |
| **Average TAT** | Avg TAT | `Total TAT / Jumlah Pelanggan` | Rata-rata total waktu yang dihabiskan seluruh pelanggan. |
| **Average WT** | Avg WT | `Total WT / Jumlah Pelanggan` | Rata-rata waktu tunggu seluruh pelanggan. |

---

## 🛠️ Fitur Utama Program
1. **Input Dinamis:** Menerima input jumlah pelanggan, nama, waktu kedatangan, dan lama pelayanan secara interaktif.
2. **Auto-Sorting:** Mengurutkan antrean secara otomatis berdasarkan waktu kedatangan terkecil (FCFS).
3. **Deteksi Kasir Nganggur (Idle Time):** Program dapat mendeteksi dan menampilkan kapan kasir tidak melakukan aktivitas karena belum ada pelanggan yang datang.
4. **Visualisasi Gantt Chart:** Menampilkan *timeline* pelayanan kasir secara visual di terminal.
5. **Ekspor Hasil:** Menyediakan opsi untuk menyimpan laporan hasil kalkulasi ke dalam file teks (`.txt`).

---

## 🚀 Alur Jalannya Program (Flowchart Logis)


STEP 1: Mulai program
   │
STEP 2: Input jumlah pelanggan (n)
   │
STEP 3: Looping input (Nama, Jam Datang, Lama Layanan) sebanyak n kali
   │
STEP 4: Tampilkan data mentah pelanggan
   │
STEP 5: Urutkan data berdasarkan Jam Datang (Kondisi FCFS)
   │
STEP 6: Set Waktu Sekarang = 0
   │
STEP 7: Evaluasi tiap pelanggan:
        ├── JIKA Waktu Sekarang < Jam Datang ──> Kasir NGANGGUR (Lompat ke Jam Datang)
        └── JIKA SUDAH Datang ──> Hitung Mulai, Selesai, TAT, dan WT
   │
STEP 8: Cetak Gantt Chart ke Terminal
   │
STEP 9: Tampilkan Tabel Hasil Perhitungan Akhir beserta Rata-rata (Avg WT & TAT)
   │
STEP 10: Opsi simpan laporan ke file teks (.txt)
   │
STEP 11: Selesai



---


## 📊 Contoh Hasil Pengujian (Test Case)

### Input Pengujian (Fitur Kasir Nganggur):

Jika kamu ingin menguji fitur kasir nganggur, kamu bisa mencoba memasukkan data berikut:

* **Pelanggan 1:** Fani, Datang: 5, Lama Layanan: 4
* **Pelanggan 2:** Gilang, Datang: 12, Lama Layanan: 6
* **Pelanggan 3:** Hani, Datang: 20, Lama Layanan: 3

### Output Laporan Berhasil (`hasil_fcfs.txt`):

============================================================
  HASIL SIMULASI FCFS - ANTRIAN KASIR MINIMARKET
============================================================

DATA PELANGGAN:
No   Nama         Datang    Lama Layanan
---------------------------------------------
1    rey          3         4
2    ran          5         10
3    run          7         9

Urutan Pelayanan: rey -> ran -> run

HASIL PERHITUNGAN:
Nama         Datang  Lama  Selesai  TAT   WT
--------------------------------------------------
rey          3       4     7        4     0
ran          5       10    17       12    2
run          7       9     26       19    10
--------------------------------------------------

Average Waiting Time    = 4.00 menit
Average Turnaround Time = 11.67 menit
