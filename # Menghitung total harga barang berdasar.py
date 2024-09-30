# Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian
print("Nama: Jemis Movid")
print("NIM: 2409116070")

# Sigh Up
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

# Menu kalkulasi
            perintah=""
            while True:
                pilihan = int(input("\n1. Pulang, 2. Calculator: "))
                if pilihan == 1:
                    break
                elif pilihan == 2:
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
                else:
                    print("error")
        else:
            print("\nData anda tidak sesuai")
    else:
        print("error")