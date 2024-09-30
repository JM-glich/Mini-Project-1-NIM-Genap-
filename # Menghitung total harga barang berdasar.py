# Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian
# ---------------------------------------------------------------------------------
# Baris 5 - 6 untuk menampilkan nama dan NIM menggunakan command print
# ---------------------------------------------------------------------------------
print("Nama: Jemis Movid")
print("NIM: 2409116070")

# Sigh Up
# ---------------------------------------------------------------------------------
# Baris 12 - 27 adalah code untuk login sederhana dengan menggunakan looping.
# ---------------------------------------------------------------------------------
Sigh_up = ""
while True:
    print("\nPilih Opsi")
    pilihan = int(input("1. Pulang, 2. Sign Up: "))
    if pilihan == 1:
        print("Terima Kasih")
        break
    elif pilihan == 2:
        Nama = input("\nMasukan nama:  ")
        NIM = int(input("Masukan NIM:  "))

        print("\nData sudah terekam")

        nama = input("Masukan nama anda kembali:  ")
        nim = int(input("Masukan NIM anda kembali:  "))

        if Nama == nama and NIM == nim:

# Memasukan input harga barang dan jumlah barang
# --------------------------------------------------------------------------------
# Baris 33 - 52 adalah kode untuk melakukan perhitungan total harga barang dengan menggunakan command if,elif dan else. Selain itu juga menggunakan command while True untuk melakukan looping atau pengulangan.
# --------------------------------------------------------------------------------
            perintah=""
            while True:
                        harga_barang = int(input("\nMasukan harga barang Rp. "))
                        jumlah_pembelian = int(input("Masukan jumlah barang: "))
                        total = harga_barang * jumlah_pembelian
                        if total > 250000:
                            total_diskon = total * 0.75
                            print(f"Rp.{total_diskon}")
                        elif total < 0:
                            print("idk")
                        else:
                            print("\nTotal pembayaran: ")
                            print(f"Rp{total}")
                        ulangi = input("""\nIngin mengulangi perhitungan lagi? 
Ya/Tidak:
""")
                        if ulangi == "Ya":
                            continue
                        elif ulangi == "Tidak":
                            print("\n~Terima Kasih~")
                            break
                        else:
                            print("error")
                            break
                        
# Commend lainnya
# ---------------------------------------------------------------------------------
# Baris 57 - 60 adalah untuk proses jika terdapat kesalahan pengisisan data atau lainnya
# ---------------------------------------------------------------------------------
        else:
            print("\nData anda tidak sesuai")
    else:
        print("error")
