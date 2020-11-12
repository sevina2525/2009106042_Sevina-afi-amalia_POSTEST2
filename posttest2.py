import os
import time

belanja = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print("Selamat datang di toko kami")
    print("========================")
    print("\tCatalog")
    print("========================")
    print("1. Baju")
    print("2. Celana")
    print("3. Sepatu")
    print("4. Keluar")
    catalog = str(input("masukkan pilihan anda> "))

    if catalog=="1":
        clear_screen()
        print("========================")
        print("\tCatalog Baju")
        print("========================")
        print("1. Little Indian")
        print("2. Nevada")
        catalog_baju = str(input("masukkan pilihan anda> "))
        if catalog_baju =="1":
            belanja.insert(0,"Little Indian")
            print("Harga: Rp. 100000")
            jumlah = int(input("jumlah barang> "))
            total = 100000*jumlah
            print("total: Rp. %d" % (total))
            bayar = float(input("bayar> "))
            if bayar >= total:
                print("kembalian: Rp. %d" % (bayar-total))
                print("keterangan: %s | lunas" % (belanja[0]))
                back_to_menu()
            else:
                print("uang anda tidak cukup!")
                time.sleep(2)
                menu()
        elif catalog_baju =="2":
            belanja.insert(0,"Nevada")
            print("Harga: Rp. 200000")
            jumlah = int(input("jumlah barang> "))
            total = 200000*jumlah
            print("total: Rp. %d" % (total))
            bayar = float(input("bayar> "))
            if bayar >= total:
                print("kembalian: Rp. %d" % (bayar-total))
                print("keterangan: %s | lunas" % (belanja[0]))
                back_to_menu()
            else:
                print("uang anda tidak cukup!")
                time.sleep(2)
                menu()
        else:
            print("produk tidak ditemukan, silahkan ulangi")
            time.sleep(2)
            menu()
    elif catalog=="2":
        clear_screen()
        print("========================")
        print("\tCatalog Celana")
        print("========================")
        print("1. Aeropostale")
        print("2. Agatha")
        catalog_celana = str(input("masukkan pilihan anda> "))
        if catalog_celana =="1":
            belanja.insert(0,"Aeropostale")
            print("Harga: Rp. 100000")
            jumlah = int(input("jumlah barang> "))
            total = 100000*jumlah
            print("total: Rp. %d" % (total))
            bayar = float(input("bayar> "))
            if bayar >= total:
                print("kembalian: Rp. %d" % (bayar-total))
                print("keterangan: %s | lunas" % (belanja[0]))
                back_to_menu()
            else:
                print("uang anda tidak cukup!")
                time.sleep(2)
                menu()
        elif catalog_celana =="2":
            belanja.insert(0,"Agatha")
            print("Harga: Rp. 200000")
            jumlah = int(input("jumlah barang> "))
            total = 200000*jumlah
            print("total: Rp. %d" % (total))
            bayar = float(input("bayar> "))
            if bayar >= total:
                print("kembalian: Rp. %d" % (bayar-total))
                print("keterangan: %s | lunas" % (belanja[0]))
                back_to_menu()
            else:
                print("uang anda tidak cukup!")
                time.sleep(2)
                menu()
        else:
            print("produk tidak ditemukan, silahkan ulangi")
            time.sleep(2)
            menu()
    elif catalog=="3":
        clear_screen()
        print("========================")
        print("\tCatalog Sepatu")
        print("========================")
        print("1. Adidas")
        print("2. Fila")
        catalog_sepatu = str(input("masukkan pilihan anda> "))
        if catalog_sepatu =="1":
            belanja.insert(0,"Adidas")
            print("Harga: Rp. 100000")
            jumlah = int(input("jumlah barang> "))
            total = 100000*jumlah
            print("total: Rp. %d" % (total))
            bayar = float(input("bayar> "))
            if bayar >= total:
                print("kembalian: Rp. %d" % (bayar-total))
                print("keterangan: %s | lunas" % (belanja[0]))
                back_to_menu()
            else:
                print("uang anda tidak cukup!")
                time.sleep(2)
                menu()
        elif catalog_sepatu =="2":
            belanja.insert(0,"Fila")
            print("Harga: Rp. 300000")
            jumlah = int(input("jumlah barang> "))
            total = 300000*jumlah
            print("total: Rp. %d" % (total))
            bayar = float(input("bayar> "))
            if bayar >= total:
                print("kembalian: Rp. %d" % (bayar-total))
                print("keterangan: %s | lunas" % (belanja[0]))
                back_to_menu()
            else:
                print("uang anda tidak cukup!")
                time.sleep(2)
                menu()
        else:
            print("produk tidak ditemukan, silahkan ulangi")
            time.sleep(2)
            menu()
    elif catalog=="4":
        tanya()
    else :
        print("produk tidak ditemukan, silahkan ulangi")
        time.sleep(2)
        menu()

def tanya():
    keluar=input("Anda yakin ingin keluar?(y/t): ")
    if keluar=="y":
        print("keluar")
        time.sleep(2)
        exit()
    else :
        menu()
    
def back_to_menu():
    print("\n") 
    input("Tekan Enter untuk kembali...")
    menu()

menu()
