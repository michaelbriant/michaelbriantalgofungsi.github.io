def print_header():
    print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
    print('@  @  @ @ @     @    @ @   @ @     @')
    print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
    print('@  @  @ @ @     @    @ @   @ @     @')
    print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

def ucapan_selamat(nama, jam_kerja):
    if 6.00 <= jam_kerja <= 12.00:
        return f"Selamat pagi {nama}\n"
    elif 12.00 <= jam_kerja <= 15.00:
        return f"Selamat siang {nama}\n"
    elif 15.00 <= jam_kerja <= 18.00:
        return f"Selamat sore {nama}\n"
    elif 18.00 <= jam_kerja <= 24.00:
        return f"Selamat malam {nama}\n"

def input_jam_kerja(prompt):
    return float(input(prompt))

def hitung_gaji(nama, jam_masuk, jam_keluar):
    waktu_kerja = jam_keluar - jam_masuk
    gaji_per_hari = 175000

    if waktu_kerja <= 8:
        gaji_total = gaji_per_hari
    else:
        gaji_lembur = (int(waktu_kerja) - 8) * 15000
        gaji_total = gaji_per_hari + gaji_lembur

    return gaji_per_hari, gaji_lembur, gaji_total, waktu_kerja

def print_rincian_gaji(nama, waktu_kerja, gaji_per_hari, gaji_lembur, gaji_total):
    print('===== Rincian Gaji Harian =====')
    print(f"Nama           : {nama}")
    print(f"Total jam kerja: {int(waktu_kerja)} jam")
    print(f"Gaji harian    : Rp. {gaji_per_hari}")
    print(f"Lembur         : Rp. {gaji_lembur:.2f} ({int(waktu_kerja - 8)} jam x Rp.15000)")
    print(f"Total          : Rp. {gaji_total:.2f}")

def main():
    print_header()
    print("\n===== HITUNGAN GAJI =====\n")

    # Input nama
    nama = input("Nama: ")

    # Input jam kerja
    jam_masuk_kerja = input_jam_kerja('Jam masuk kantor: ')

    # Ucapan selamat berdasarkan waktu
    print(ucapan_selamat(nama, jam_masuk_kerja))

    # Input jam keluar kerja
    jam_keluar_kerja = input_jam_kerja('Jam pulang kantor: ')

    # Ucapan selamat berdasarkan waktu
    print(ucapan_selamat(nama, jam_keluar_kerja))

    # Hitung dan tampilkan rincian gaji
    gaji_per_hari, gaji_lembur, gaji_total, waktu_kerja = hitung_gaji(nama, jam_masuk_kerja, jam_keluar_kerja)
    print_rincian_gaji(nama, waktu_kerja, gaji_per_hari, gaji_lembur, gaji_total)

    print("===== TERIMAKASIH =====")

# Panggil fungsi main()
main()
