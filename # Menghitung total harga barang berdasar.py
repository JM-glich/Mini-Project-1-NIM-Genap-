# Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian
# ---------------------------------------------------------------------------------
# Baris 5 - 6 untuk menampilkan nama dan NIM menggunakan command print
# ---------------------------------------------------------------------------------
print("Nama: Jemis Movid")
print("NIM: 2409116070")

# Sigh Up
# ---------------------------------------------------------------------------------
# Baris 9 - 24 adalah code untuk login sederhana dengan menggunakan looping.
# ---------------------------------------------------------------------------------
Sigh_up = ""
while True:
    print("\nPilih Opsi")
    pilihan = int(input("1. Pulang, 2. Sign Up: "))
    if pilihan == 1:
        break
    elif pilihan == 2:
        Nama = input("\nMasukan nama:  ")
        NIM = int(input("Masukan NIM:  "))

        print("\nData sudah terekam")

        nama = input("Masukan nama anda kembali:  ")
        nim = int(input("Masukan NIM anda kembali:  "))

        if Nama == nama and NIM == nim:

# Looping ke-2
# --------------------------------------------------------------------------------
# Baris 30 - 35 adalah untuk commend jika memilih opsi 1) maka akan kembali ke menu pertama dan jika memilih opsi 2) maka akan lanjut ke menu kalkulasi
# --------------------------------------------------------------------------------
            perintah=""
            while True:
                pilihan = int(input("\n1. Pulang, 2. Calculator: "))
                if pilihan == 1:
                    break
                elif pilihan == 2:
# Menu kalkulasi
# ---------------------------------------------------------------------------------
# Baris 40 - 50 adalah proses kalkulasi dengan mengunakan command if, elif dan else. 
# ---------------------------------------------------------------------------------
                        harga_barang = int(input("\nHarga barang Rp. "))
                        jumlah_pembelian = int(input("Jumlah barang: "))
                        total = harga_barang * jumlah_pembelian
                        if total > 250000:
                            total_diskon = total * 0.75
                            print(f"Rp.{total_diskon}")
                        elif total < 0:
                            print("idk")
                        else:
                            print("\nTotal pembayaran: ")
                            print(f"Rp{total}")

# Commend lainnya
# ---------------------------------------------------------------------------------
# Baris 56 - 61 adalah untuk proses jika terdapat kesalahan pengisisan data atau lainnya
# ---------------------------------------------------------------------------------
                else:
                    print("error")
        else:
            print("\nData anda tidak sesuai")
    else:
        print("error")

