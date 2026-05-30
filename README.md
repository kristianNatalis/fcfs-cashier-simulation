
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

