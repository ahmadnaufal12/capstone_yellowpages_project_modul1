from tabulate import tabulate

# Daftar Menu data Yellow Pages
dataYellowPages = [
    {"kode": "1", "Sektor": "FnB", "Nama": "Sari Rasa", "Alamat": "Jl. Kebon Jeruk No. 4", "Nomor Telepon": "089712345678", "Kota": "Jakarta", "Status": "Aktif"},
    {"kode": "2", "Sektor": "FnB", "Nama": "Kopi Kita", "Alamat": "Jl. Melati No. 10", "Nomor Telepon": "087876543621", "Kota": "Bandung", "Status": "Aktif"},
    {"kode": "3", "Sektor": "Pariwisata", "Nama": "Guest House OPO", "Alamat": "Jl. Pantai No. 15", "Nomor Telepon": "087363234567", "Kota": "Bali", "Status": "Aktif"},
    {"kode": "4", "Sektor": "Jasa", "Nama": "Kita Loundry", "Alamat": "Jl. Sawi No. 8", "Nomor Telepon": "087634567890", "Kota": "Yogyakarta", "Status": "Aktif"}
]

# Fungsi validasi input
def validate_sector(sector):
    return sector.isalpha()
def validate_name(name):
    return all(part.isalpha() for part in name.split())
def validate_address(address):
    return len(address) >= 5
def validate_phone(phone):
    return phone.isdigit() and len(phone) >= 10
def validate_city(city):
    return all(part.isalpha() for part in city.split())
# Daftar penyimpanan sementara
temporary_backup = []

def menu_utama():
    while True:
        print('\n************* SELAMAT DATANG DI YELLOW PAGES PURWADHIKA *************')
        print('\n'.join([
            "1. View Data",
            "2. Create Data",
            "3. Update Data",
            "4. Delete Data",
            "5. Search Data",
            "6. Backup Data",
            "7. Exit"
        ]))

        option = input("\nSilahkan Pilih Menu (1-7):\n")
        if option == '1':
            view_data()
        elif option == '2':
            create_data()
        elif option == '3':
            update_data()
        elif option == '4':
            delete_data()
        elif option == '5':
            search_data()
        elif option == '6':
            backup_data()
        elif option == '7':
            print('\nThank you and good bye!\n')
            break
        else:
            print('\nOpsi menu tidak tersedia, silahkan input angka 1-7\n')

def view_data():
    while True:
        print('\n************* MENU VIEW DATA *************')
        print('1. Menampilkan seluruh data')
        print('2. Menampilkan data tertentu')
        print('3. Sortir Data')
        print('4. Kembali ke Menu Utama\n')

        option = input("Silahkan pilih sub-menu (1-4):\n")

        if option == '1':
            if not dataYellowPages:
                print('Data Tidak Tersedia')
            else:
                print('Daftar Perusahaan:\n')
                print(tabulate(dataYellowPages, headers='keys', tablefmt='fancy_grid'))

        elif option == '2':
            nama_dicari = input("\nMasukkan nama perusahaan yang dicari:\n").title()
            found = next((data for data in dataYellowPages if data["Nama"] == nama_dicari), None)
            if found:
                print(f"\nData ditemukan:\nSektor: {found['Sektor']}\nNama: {found['Nama']}\nAlamat: {found['Alamat']}\nNomor Telepon: {found['Nomor Telepon']}\nKota: {found['Kota']}\nStatus: {found['Status']}")
            else:
                print("\nData tidak ditemukan.")

        elif option == '3':
            sort_criteria = input("\nSort berdasarkan (Nama/Kota):\n").title()
            if sort_criteria in ['Nama', 'Kota']:
                dataYellowPages.sort(key=lambda x: x[sort_criteria])
                # Update kode setelah sorting
                for index, item in enumerate(dataYellowPages):
                    item['kode'] = str(index + 1)
                print("\nData telah diurutkan.")
            else:
                print("\nKriteria sort tidak valid.")

        elif option == '4':
            return
        else:
            print('\nOpsi tidak tersedia, silahkan input angka 1-4\n')


def create_data():
    while True:
        print('\n************* MENU CREATE DATA *************')
        print('1. Menambahkan data kontak')
        print('2. Kembali ke Menu Utama\n')

        option = input("Silahkan pilih sub-menu (1-2):\n")

        if option == '1':
            next_code = str(len(dataYellowPages) + 1)
            tambah_sektor = input('\nSilahkan input Sektor: \n').title()
            while not validate_sector(tambah_sektor):
                print("Sektor hanya boleh berupa huruf.")
                tambah_sektor = input('\nSilahkan input Sektor yang benar: \n').title()

            tambah_nama = input('\nSilahkan input Nama: \n').title()
            while not validate_name(tambah_nama):
                print("Nama hanya boleh berupa huruf dan spasi.")
                tambah_nama = input('\nSilahkan input Nama yang benar: \n').title()

            # Periksa duplikat berdasarkan Nama
            if any(data['Nama'] == tambah_nama for data in dataYellowPages):
                print("\nData dengan nama tersebut sudah ada.")
                continue

            tambah_alamat = input('\nSilahkan input Alamat: \n').title()
            while not validate_address(tambah_alamat):
                print("Alamat terlalu pendek, minimal 5 karakter.")
                tambah_alamat = input('\nSilahkan input Alamat yang benar: \n').title()

            tambah_nomor_telepon = input('\nSilahkan input Nomor Telepon (hanya angka): \n')
            while not validate_phone(tambah_nomor_telepon):
                print("Nomor telepon harus angka dan minimal 10 digit.")
                tambah_nomor_telepon = input('\nSilahkan input Nomor Telepon yang benar: \n')

            tambah_kota = input('\nSilahkan input Kota: \n').title()
            while not validate_city(tambah_kota):
                print("Nama kota hanya boleh berupa huruf dan spasi.")
                tambah_kota = input('\nSilahkan input Kota yang benar: \n').title()

            while True:
                simpan = input('\nApakah data akan disimpan? (yes/no): \n').lower()
                if simpan == 'yes':
                    dataYellowPages.append({
                        'kode': next_code,
                        'Sektor': tambah_sektor,
                        'Nama': tambah_nama,
                        'Alamat': tambah_alamat,
                        'Nomor Telepon': tambah_nomor_telepon,
                        'Kota': tambah_kota,
                        'Status': 'Aktif'  # Entri baru defaultnya adalah 'Aktif'
                    })
                    print('\nData saved.')
                    break
                elif simpan == 'no':
                    print("\nData not saved.")
                    break
                else:
                    print("\nInput tidak valid. Silakan masukkan 'yes' atau 'no'.")

        elif option == '2':
            return
        else:
            print('\nOpsi tidak tersedia, silahkan input angka 1-2\n')


def update_data():
    while True:
        print('\n************* MENU UPDATE DATA *************')
        print('1. Update Data Kontak')
        print('2. Kembali ke Menu Utama\n')

        option = input("Silahkan pilih sub-menu (1-2):\n")

        if option == '1':
            kode_kontak = input('\nSilahkan input kode kontak yang akan diupdate:\n')
            found = next((j for j in dataYellowPages if kode_kontak == j['kode']), None)

            if found:
                print('\nData kontak yang akan diupdate:')
                print(f"Sektor: {found['Sektor']}, Nama: {found['Nama']}, Alamat: {found['Alamat']}, No HP: {found['Nomor Telepon']}, Kota: {found['Kota']}, Status: {found['Status']}")

                while True:
                    option_update = input("\nApakah data akan diupdate (yes/no):\n").lower()
                    if option_update == 'yes':
                        while True:
                            kode_update = input('\nSilahkan input kolom yang akan diupdate (Sektor/Nama/Alamat/Nomor Telepon/Kota/Status):\n').title()

                            if kode_update in ['Sektor', 'Nama', 'Alamat', 'Nomor Telepon', 'Kota', 'Status']:
                                print(f"\nData lama: {found[kode_update].capitalize()}")
                                new_value = input(f'\nSilahkan input {kode_update} yang baru:\n')

                                if kode_update == 'Sektor' and validate_sector(new_value):
                                    found[kode_update] = new_value.title()
                                elif kode_update == 'Nama' and validate_name(new_value):
                                    if any(data['Nama'] == new_value for data in dataYellowPages if data['kode'] != kode_kontak):
                                        print("\nNama sudah ada, tidak bisa diperbarui.")
                                        continue
                                    found[kode_update] = new_value.title()
                                elif kode_update == 'Alamat' and validate_address(new_value):
                                    found[kode_update] = new_value.title()
                                elif kode_update == 'Nomor Telepon' and validate_phone(new_value):
                                    if any(data['Nomor Telepon'] == new_value for data in dataYellowPages if data['kode'] != kode_kontak):
                                        print("\nNomor telepon sudah ada, tidak bisa diperbarui.")
                                        continue
                                    found[kode_update] = new_value
                                elif kode_update == 'Kota' and validate_city(new_value):
                                    found[kode_update] = new_value.title()
                                else:
                                    print("\nInput tidak valid, silahkan coba lagi.")
                                    continue

                                print(f"\nData baru: {found[kode_update].capitalize()}")
                                print("\nData berhasil diupdate.\n")
                                break
                            else:
                                print("\nKolom yang Anda pilih tidak valid. Silahkan pilih antara Sektor/Nama/Alamat/Nomor Telepon/Kota/Status.")
                                continue
                        break
                    elif option_update == 'no':
                        print("\nData tidak diupdate.\n")
                        break
            else:
                print('\nData yang Anda cari tidak ada\n')

        elif option == '2':
            return
        else:
            print('\nOpsi tidak tersedia, silahkan input angka 1-2\n')


def delete_data():
    while True:
        print('\n************* MENU DELETE DATA *************')
        print('1. Hapus Data Kontak Berdasarkan kode')
        print('2. Kembali ke Menu Utama\n')

        option = input("Silahkan pilih sub-menu (1-2):\n")

        if option == '1':
            kode_hapus = input('\nMasukkan kode kontak yang akan dihapus:\n')

            if not kode_hapus.strip():
                print("\nKode tidak boleh kosong. Silakan masukkan kode yang valid.")
                continue

            found = next((data for data in dataYellowPages if data['kode'] == kode_hapus), None)

            if found:
                dataYellowPages.remove(found)
                print(f"\nData dengan kode {kode_hapus} berhasil dihapus.")
            else:
                print("\nData tidak ditemukan.")

        elif option == '2':
            return
        else:
            print('\nOpsi tidak tersedia, silahkan input angka 1-2\n')

def search_data():
    print('\n************* MENU SEARCH DATA *************')
    print('1. Search by Name\n2. Search by Sector\n3. Search by City\n4. Kembali ke Menu Utama\n')

    option = input("Silahkan pilih sub-menu (1-4):\n")
    results = []
    queries = {'1': 'Nama', '2': 'Sektor', '3': 'Kota'}

    if option in queries:
        query = input(f"Masukkan {queries[option]} yang dicari:\n").lower()
        results = [data for data in dataYellowPages if query in data[queries[option]].lower()]
    elif option == '4':
        return
    else:
        print('\nOpsi tidak tersedia, silahkan input angka 1-4\n')
        return

    print('Hasil pencarian:\n')
    print(tabulate(results, headers='keys', tablefmt='fancy_grid') if results else "\nData tidak ditemukan.")

def backup_data():
    global temporary_backup  # Akses variabel global
    global dataYellowPages   # Declare it as global here

    while True:
        print('\n************* MENU BACKUP DATA *************')
        print('1. Backup Data')
        print('2. Restore Data')
        print('3. View Current Data')
        print('4. Kembali ke Menu Utama\n')

        option = input("Silahkan pilih sub-menu (1-4):\n")

        if option == '1':
            temporary_backup = dataYellowPages.copy()  # Buat salinan data saat ini
            print("\nData telah berhasil dibackup ke penyimpanan sementara.")

        elif option == '2':
            if temporary_backup:
                dataYellowPages.clear()
                dataYellowPages.extend(temporary_backup)  # Pulihkan data dari cadangan
                print("\nData telah berhasil dipulihkan dari backup.")
            else:
                print("\nTidak ada data backup yang tersedia.")

        elif option == '3':
            view_data()  # Panggil fungsi view_data yang ada

        elif option == '4':
            return

        else:
            print('\nOpsi tidak tersedia, silahkan input angka 1-4\n')


# Start the program
menu_utama()
