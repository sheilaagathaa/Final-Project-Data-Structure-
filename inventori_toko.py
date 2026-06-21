import csv
import os

# =========================
#   KONFIGURASI FILE CSV
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "barang.csv")


# =========================
#           QUEUE 
# =========================
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        return self.items


# =========================
#     INISIALISASI CSV
# =========================
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID Barang",
            "Nama Barang",
            "Kategori",
            "Harga",
            "Stok"
        ])


# =========================
#     LOAD & SAVE DATA
# =========================
def muat_data():
    data_base = {}
    try:
        with open(CSV_FILE, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_base[row["ID Barang"]] = {
                    "Nama Barang": row["Nama Barang"],
                    "Kategori": row["Kategori"],
                    "Harga": float(row["Harga"]),
                    "Stok": int(row["Stok"])
                }
    except FileNotFoundError:
        pass
    return data_base

def simpan_data(data_base):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "ID Barang",
            "Nama Barang",
            "Kategori",
            "Harga",
            "Stok"
        ]
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        for id_barang, info in data_base.items():
            writer.writerow({
                "ID Barang": id_barang,
                "Nama Barang": info["Nama Barang"],
                "Kategori": info["Kategori"],
                "Harga": info["Harga"],
                "Stok": info["Stok"]
            })


# =========================
#       OPERASI CRUD
# =========================
def tambah_barang(data_base):
    print("\n===== TAMBAH BARANG =====")
    id_barang = input("ID Barang      : ").upper()
    if id_barang in data_base:
        print("ID Barang Sudah Ada!")
        return
    nama_barang = input("Nama Barang    : ")
    kategori = input("Kategori       : ")
    harga = float(input("Harga          : "))
    stok = int(input("Stok           : "))

    data_base[id_barang] = {
        "Nama Barang": nama_barang,
        "Kategori": kategori,
        "Harga": harga,
        "Stok": stok
    }

    simpan_data(data_base)
    print("Barang Berhasil Ditambahkan!")

def tampilkan_barang(data_base):
    print("\n" + "=" * 90)
    print("DAFTAR BARANG".center(90))
    print("=" * 90)

    if not data_base:
        print("Tidak Ada Barang!")
        return
    print("{:<10} {:<35} {:<15} {:<15} {:<10}".format(
        "ID",
        "Nama Barang",
        "Kategori",
        "Harga",
        "Stok"
    ))
    print("-" * 90)

    for id_barang, info in data_base.items():
        print("{:<10} {:<35} {:<15} Rp {:<11,.0f} {:<10}".format(
            id_barang,
            info["Nama Barang"],
            info["Kategori"],
            info["Harga"],
            info["Stok"]
        ))

def update_barang(data_base):
    print("\n===== UPDATE BARANG =====")
    id_barang = input("Masukkan ID Barang : ").upper()
    if id_barang not in data_base:
        print("Barang Tidak Ditemukan!")
        return

    data = data_base[id_barang]

    nama = input(f"Nama ({data['Nama Barang']}) : ")
    kategori = input(f"Kategori ({data['Kategori']}) : ")
    harga = input(f"Harga ({data['Harga']}) : ")
    stok = input(f"Stok ({data['Stok']}) : ")

    if nama:
        data["Nama Barang"] = nama
    if kategori:
        data["Kategori"] = kategori
    if harga:
        data["Harga"] = float(harga)
    if stok:
        data["Stok"] = int(stok)

    simpan_data(data_base)
    print("Data Berhasil Diperbarui!")

def hapus_barang(data_base):
    print("\n===== HAPUS BARANG =====")
    id_barang = input("Masukkan ID Barang : ").upper()

    if id_barang in data_base:
        del data_base[id_barang]
        simpan_data(data_base)
        print("Barang Berhasil Dihapus!")
    else:
        print("Barang Tidak Ditemukan!")


# =========================
#        SEARCHING
# =========================
def cari_barang(data_base):
    print("\n===== CARI BARANG =====")
    keyword = input(
        "Masukkan ID / Nama Barang : "
    ).lower()

    ditemukan = False

    for id_barang, info in data_base.items():
        if (
            keyword == id_barang.lower()
            or keyword in info["Nama Barang"].lower()
        ):

            print("\nData Ditemukan")
            print("ID Barang :", id_barang)
            print("Nama      :", info["Nama Barang"])
            print("Kategori  :", info["Kategori"])
            print("Harga     :", info["Harga"])
            print("Stok      :", info["Stok"])

            ditemukan = True
    if not ditemukan:
        print("Barang Tidak Ditemukan!")


# =========================
#       BARANG MASUK
# =========================
def barang_masuk(data_base):
    print("\n===== BARANG MASUK =====")
    id_barang = input("ID Barang : ").upper()

    if id_barang not in data_base:
        print("Barang Tidak Ditemukan!")
        return

    jumlah = int(input("Jumlah Masuk : "))

    data_base[id_barang]["Stok"] += jumlah

    simpan_data(data_base)
    print("Stok Berhasil Ditambahkan!")


# =========================
#       QUEUE RESTOCK
# =========================
antrian_stok = Queue()


# =========================
#       BARANG KELUAR
# =========================
def barang_keluar(data_base):
    print("\n===== BARANG KELUAR =====")
    id_barang = input("ID Barang : ").upper()

    if id_barang not in data_base:
        print("Barang Tidak Ditemukan!")
        return

    jumlah = int(input("Jumlah Keluar : "))

    if jumlah > data_base[id_barang]["Stok"]:
        print("Stok Tidak Mencukupi!")
        return

    data_base[id_barang]["Stok"] -= jumlah

    stok_sisa = data_base[id_barang]["Stok"]

    if (
        stok_sisa <= 5
        and id_barang not in antrian_stok.display()
    ):
        antrian_stok.enqueue(id_barang)

        print("\nPERINGATAN!")
        print("Stok Menipis!")
        print("Masuk Antrean Restock")

    simpan_data(data_base)
    print("Barang Keluar Berhasil!")
    print("Sisa Stok :", stok_sisa)


# =========================
#       SORTING STOK
# =========================
def urutan_stok(data_base):
    print("\n===== STOK PALING SEDIKIT =====")

    data = list(data_base.items())
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            if (
                data[j][1]["Stok"]
                >
                data[j + 1][1]["Stok"]
            ):
                data[j], data[j + 1] = (
                    data[j + 1],
                    data[j]
                )

    for id_barang, info in data:
        print(
            id_barang,
            "-",
            info["Nama Barang"],
            "- Stok:",
            info["Stok"]
        )


# =========================
#       SORTING NAMA
# =========================
def urutkan_nama(data_base):
    print("\n===== URUTKAN NAMA A-Z =====")
    data = list(data_base.items())
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            nama1 = data[j][1]["Nama Barang"].lower()
            nama2 = data[j + 1][1]["Nama Barang"].lower()
            if nama1 > nama2:
                data[j], data[j + 1] = (
                    data[j + 1],
                    data[j]
                )

    for id_barang, info in data:
        print(
            id_barang,
            "-",
            info["Nama Barang"]
        )


# =========================
#       LIHAT ANTREAN
# =========================
def lihat_antrian_restock(data_base):
    print("\n===== ANTREAN RESTOCK =====")

    if antrian_stok.is_empty():
        print("Tidak Ada Antrean.")
        return

    nomor = 1

    for item in antrian_stok.display():
        print(
            nomor,
            ".",
            item,
            "-",
            data_base[item]["Nama Barang"]
        )

        nomor += 1


# =========================
#      PROSES RESTOCK
# =========================
def proses_restock(data_base):
    print("\n===== PROSES RESTOCK =====")
    if antrian_stok.is_empty():
        print("Tidak Ada Antrean.")
        return

    id_barang = antrian_stok.dequeue()
    jumlah = int(input("Jumlah Restock : "))

    data_base[id_barang]["Stok"] += jumlah
    stok_baru = data_base[id_barang]["Stok"]

    # Jika setelah restock ternyata masih dikit, masukkan kembali ke antrean paling belakang.
    if stok_baru <= 5:
        antrian_stok.enqueue(id_barang)
        print("\nPERINGATAN! Stok baru masih di bawah batas minimum (<= 5).")
        print("Barang dimasukkan kembali ke antrean restock.")

    simpan_data(data_base)

    print("Restock Berhasil!")
    print("Barang    :", data_base[id_barang]["Nama Barang"])
    print("Stok Baru :", stok_baru)


# =========================
#    ANALISIS INVENTORI
# =========================
def analisis_inventori(data_base):
    print("\n===== ANALISIS INVENTORI =====")

    if not data_base:
        print("Data Kosong!")
        return

    total_barang = len(data_base)

    total_stok = 0
    total_nilai = 0

    for info in data_base.values():
        total_stok += info["Stok"]
        total_nilai += (
            info["Harga"]
            *
            info["Stok"]
        )

    stok_maks = max(
        data_base.items(),
        key=lambda x: x[1]["Stok"]
    )

    stok_min = min(
        data_base.items(),
        key=lambda x: x[1]["Stok"]
    )

    print("Jumlah Jenis Barang :", total_barang)
    print("Total Stok Barang   :", total_stok)
    print(f"Nilai Inventori     : Rp {total_nilai:,.0f}")
    print(
        "Stok Terbanyak      :",
        stok_maks[1]["Nama Barang"],
        f"({stok_maks[1]['Stok']})"
    )
    print(
        "Stok Tersedikit     :",
        stok_min[1]["Nama Barang"],
        f"({stok_min[1]['Stok']})"
    )


# =========================
#        MENU UTAMA
# =========================
def main():
    data_base = muat_data()
    while True:
        print("\n" + "=" * 50)
        print("SISTEM INVENTORI TOKO".center(50))
        print("=" * 50)
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("6. Barang Masuk")
        print("7. Barang Keluar")
        print("8. Urutkan Stok")
        print("9. Lihat Antrean Restock")
        print("10. Proses Restock")
        print("11. Analisis Inventori")
        print("12. Urutkan Nama Barang")
        print("0. Keluar")

        pilihan = input("\nPilih Menu : ")

        if pilihan == "1":
            tambah_barang(data_base)
        elif pilihan == "2":
            tampilkan_barang(data_base)
        elif pilihan == "3":
            update_barang(data_base)
        elif pilihan == "4":
            hapus_barang(data_base)
        elif pilihan == "5":
            cari_barang(data_base)
        elif pilihan == "6":
            barang_masuk(data_base)
        elif pilihan == "7":
            barang_keluar(data_base)
        elif pilihan == "8":
            urutan_stok(data_base)
        elif pilihan == "9":
            lihat_antrian_restock(data_base)
        elif pilihan == "10":
            proses_restock(data_base)
        elif pilihan == "11":
            analisis_inventori(data_base)
        elif pilihan == "12":
            urutkan_nama(data_base)
        elif pilihan == "0":
            print("\nTerima Kasih.")
            break
        else:
            print("\nPilihan Tidak Valid!")

if __name__ == "__main__":
    main()