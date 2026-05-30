# ============================================================
# SIMULASI ALGORITMA PENJADWALAN FCFS
# Studi Kasus: Antrean Kasir Minimarket
# Mata Kuliah: Computer Organization dan Operating Systems
# Referensi: William Stallings - Operating Systems
# ============================================================

# --- BAGIAN 1: MASUKIN DATA PELANGGAN ---
print("=" * 60)
print("  SIMULASI ANTRIAN KASIR MINIMARKET")
print("  Algoritma: FCFS (First Come First Serve)")
print("  Siapa yang datang duluan, dilayani duluan")
print("=" * 60)

print("\n--- MASUKIN DATA PELANGGAN ---")
jumlah = int(input("Berapa orang pelanggan? "))

# Buat list kosong buat nyimpen data
nama_list = []
datang_list = []
lama_list = []

# Looping buat masukin data tiap pelanggan
for i in range(jumlah):
    print(f"\nPelanggan ke-{i+1}:")
    nama = input("  Nama pelanggan: ")
    datang = int(input("  Jam datang (menit ke-berapa): "))
    lama = int(input("  Lama layanan/belanja (menit): "))
    
    nama_list.append(nama)
    datang_list.append(datang)
    lama_list.append(lama)

# --- BAGIAN 2: TAMPILIN DATA YANG UDAH DIMASUKIN ---
print("\n" + "=" * 60)
print("  DATA PELANGGAN YANG DIMASUKKAN")
print("=" * 60)
print("No   Nama         Datang    Lama Layanan")
print("-" * 45)

for i in range(jumlah):
    print(f"{i+1:<5}{nama_list[i]:<13}{datang_list[i]:<10}{lama_list[i]}")

# --- BAGIAN 3: URUTKAN BERDASARKAN JAM DATANG (FCFS) ---
print("\n" + "=" * 60)
print("  PROSES PENJADWALAN FCFS")
print("=" * 60)

# Kita buat list index: [0, 1, 2, ...]
urutan = list(range(jumlah))

# Urutkan index berdasarkan jam datang (yang paling awal di depan)
for i in range(jumlah):
    for j in range(i + 1, jumlah):
        if datang_list[urutan[j]] < datang_list[urutan[i]]:
            # Tukar posisi kalau yang belakang datang lebih awal
            urutan[i], urutan[j] = urutan[j], urutan[i]

print("Urutan pelayanan berdasarkan jam datang:")
for i in range(jumlah):
    idx = urutan[i]
    print(f"  {i+1}. {nama_list[idx]} (datang menit ke-{datang_list[idx]})")

# --- BAGIAN 4: HITUNG WAKTU-WAKTU ---
print("\n" + "=" * 60)
print("  PERHITUNGAN WAKTU TIAP PELANGGAN")
print("=" * 60)

waktu_sekarang = 0  # Kasir mulai dari menit 0

# List buat nyimpen hasil perhitungan
selesai_list = []    # Jam selesai dilayani
tunggu_list = []     # Lama nunggu (Waiting Time)
total_list = []      # Total waktu dari datang sampe selesai (Turnaround Time)

# List buat Gantt chart
gantt_nama = []
gantt_mulai = []
gantt_selesai = []

# Proses tiap pelanggan sesuai urutan
for i in range(jumlah):
    idx = urutan[i]  # Ambil index pelanggan yang lagi diproses
    
    # Kalau kasir kosong tapi pelanggan belum datang, tunggu dulu
    if waktu_sekarang < datang_list[idx]:
        print(f"\n  [KASIR NGANGGUR] Menit {waktu_sekarang} - {datang_list[idx]}: Belum ada pelanggan")
        waktu_sekarang = datang_list[idx]
    
    # Kasir mulai layani pelanggan ini
    mulai = waktu_sekarang
    selesai = mulai + lama_list[idx]
    
    # Simpan data buat Gantt chart
    gantt_nama.append(nama_list[idx])
    gantt_mulai.append(mulai)
    gantt_selesai.append(selesai)
    selesai_list.append(selesai)
    
    # HITUNG TURNAROUND TIME (TAT)
    # TAT = Waktu selesai - Waktu datang
    tat = selesai - datang_list[idx]
    total_list.append(tat)
    
    # HITUNG WAITING TIME (WT)
    # WT = TAT - Lama layanan
    wt = tat - lama_list[idx]
    tunggu_list.append(wt)
    
    # Tampilin langkah perhitungan
    print(f"\n  [{nama_list[idx]}]")
    print(f"    Mulai dilayani : menit {mulai}")
    print(f"    Selesai        : menit {selesai}")
    print(f"    TAT = {selesai} - {datang_list[idx]} = {tat} menit")
    print(f"    WT  = {tat} - {lama_list[idx]} = {wt} menit")
    
    # Kasir pindah ke waktu selesai pelanggan ini
    waktu_sekarang = selesai

# --- BAGIAN 5: GANTT CHART ---
print("\n" + "=" * 60)
print("  GANTT CHART (Timeline Pelayanan Kasir)")
print("=" * 60)

# Gambar baris isi (nama pelanggan)
print("\n  ", end="")
for i in range(len(gantt_nama)):
    lebar = gantt_selesai[i] - gantt_mulai[i]
    nama = gantt_nama[i]
    # Center nama di kotak
    spasi_total = lebar * 2
    spasi_kiri = (spasi_total - len(nama)) // 2
    spasi_kanan = spasi_total - len(nama) - spasi_kiri
    print("|" + " " * spasi_kiri + nama + " " * spasi_kanan, end="")
print("|")

# Gambar garis pembatas
print("  ", end="")
for i in range(len(gantt_nama)):
    lebar = gantt_selesai[i] - gantt_mulai[i]
    print("+" + "-" * (lebar * 2), end="")
print("+")

# Gambar angka waktu di bawah
print("  ", end="")
for i in range(len(gantt_nama)):
    lebar = gantt_selesai[i] - gantt_mulai[i]
    print(f"{gantt_mulai[i]:<{lebar * 2}}", end="")
print(f"{gantt_selesai[-1]}")

# --- BAGIAN 6: TABEL HASIL AKHIR ---
print("\n" + "=" * 60)
print("  TABEL HASIL PERHITUNGAN")
print("=" * 60)
print("Nama         Datang  Lama  Selesai  TAT   WT")
print("-" * 50)

total_wt = 0
total_tat = 0

for i in range(jumlah):
    idx = urutan[i]
    print(f"{nama_list[idx]:<13}{datang_list[idx]:<8}{lama_list[idx]:<6}{selesai_list[i]:<9}{total_list[i]:<6}{tunggu_list[i]}")
    total_wt += tunggu_list[i]
    total_tat += total_list[i]

print("-" * 50)

# --- BAGIAN 7: RATA-RATA ---
rata_wt = total_wt / jumlah
rata_tat = total_tat / jumlah

print(f"\n  Rumus Average Waiting Time:")
print(f"    = (WT1 + WT2 + ... + WTn) / jumlah pelanggan")
print(f"    = {total_wt} / {jumlah}")
print(f"    = {rata_wt:.2f} menit")

print(f"\n  Rumus Average Turnaround Time:")
print(f"    = (TAT1 + TAT2 + ... + TATn) / jumlah pelanggan")
print(f"    = {total_tat} / {jumlah}")
print(f"    = {rata_tat:.2f} menit")

# --- BAGIAN 8: SIMPAN KE FILE  ---
print("\n" + "=" * 60)
print("  SIMPAN HASIL KE FILE")
print("=" * 60)

simpan = input("Mau simpan hasil ke file? (y/n): ")

if simpan.lower() == 'y':
    nama_file = input("Nama file (contoh: hasil_fcfs.txt): ") or "hasil_fcfs.txt"
    
    # Buka file buat nulis
    file = open(nama_file, "w")
    
    file.write("=" * 60 + "\n")
    file.write("  HASIL SIMULASI FCFS - ANTRIAN KASIR MINIMARKET\n")
    file.write("=" * 60 + "\n\n")
    
    file.write("DATA PELANGGAN:\n")
    file.write("No   Nama         Datang    Lama Layanan\n")
    file.write("-" * 45 + "\n")
    for i in range(jumlah):
        file.write(f"{i+1:<5}{nama_list[i]:<13}{datang_list[i]:<10}{lama_list[i]}\n")
    
    file.write(f"\nUrutan Pelayanan: ")
    for i in range(jumlah):
        idx = urutan[i]
        file.write(f"{nama_list[idx]}")
        if i < jumlah - 1:
            file.write(" -> ")
    file.write("\n\n")
    
    file.write("HASIL PERHITUNGAN:\n")
    file.write("Nama         Datang  Lama  Selesai  TAT   WT\n")
    file.write("-" * 50 + "\n")
    for i in range(jumlah):
        idx = urutan[i]
        file.write(f"{nama_list[idx]:<13}{datang_list[idx]:<8}{lama_list[idx]:<6}{selesai_list[i]:<9}{total_list[i]:<6}{tunggu_list[i]}\n")
    
    file.write("-" * 50 + "\n")
    file.write(f"\nAverage Waiting Time    = {rata_wt:.2f} menit\n")
    file.write(f"Average Turnaround Time = {rata_tat:.2f} menit\n")
    
    file.close()
    
    print(f"\n  Berhasil disimpan ke file: {nama_file}")

print("\n" + "=" * 60)
print("  SELESAI! Terima kasih.")
print("=" * 60)