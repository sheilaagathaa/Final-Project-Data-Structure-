# Final Project Data Structure
Inventory Management System Built with Python, Featuring CSV Storage, CRUD Operations, Searching, Sorting, Stack, and Queue.

---
## 👤 Identitas Mahasiswa
* **Nama:** Sheila Syah Agatha
* **NIM:** 25416255201075
* **Kelas:** IF25C
* **Mata Kuliah:** Struktur Data

---

## 🚀 Fitur Utama & Operasi CRUD
Aplikasi ini mendukung manajemen data barang secara penuh yang langsung tersinkronisasi secara real-time ke dalam file `barang.csv`:
1. **Create (Tambah Barang):** Menambahkan data barang baru lengkap dengan validasi ID unik.
2. **Read (Lihat Barang):** Menampilkan seluruh daftar barang dalam bentuk tabel yang rapi di terminal.
3. **Update (Ubah Barang):** Memperbarui informasi barang (Nama, Kategori, Harga, Stok) secara selektif berdasarkan ID.
4. **Delete (Hapus Barang):** Menghapus data barang secara permanen dari sistem basis data.

---

## 🧠 Implementasi Struktur Data & Algoritma
Sesuai dengan persyaratan teknis wajib, aplikasi ini mengimplementasikan konsep struktur data murni demi mengoptimalkan pemrosesan data:

### 1. Hash Map / Dictionary
Digunakan sebagai struktur penyimpanan basis data utama di dalam program (`data_base = {}`). Dengan memanfaatkan konsep *Key-Value pair* di mana `ID Barang` bertindak sebagai *key* unik, proses pencarian, pembaruan, dan penghapusan data dapat diakses dengan efisiensi waktu yang optimal.

### 2. Queue (Antrean Custom)
Dibuat melalui struktur kelas mandiri untuk menangani **Sistem Antrean Restock Otomatis**. Ketika transaksi barang keluar menyebabkan sisa stok berada di bawah batas minimum ($\le 5$), ID barang tersebut akan otomatis dimasukkan ke dalam antrean berprinsip *First-In, First-Out* (FIFO) untuk diprioritaskan pada menu proses restock.

### 3. Searching (Sequential Search)
Mekanisme pencarian fleksibel pada menu "Cari Barang", di mana pengguna dapat melacak item berdasarkan kecocokan ID maupun potongan kata dari nama barang secara dinamis.

### 4. Sorting (Bubble Sort)
Mengimplementasikan algoritma pengurutan Bubble Sort secara manual untuk dua kebutuhan analisis data yang berbeda:
* **Urutkan Stok:** Mengurutkan barang dari jumlah stok terkecil (skenario prioritas pengadaan kembali).
* **Urutkan Nama:** Mengurutkan nama barang secara alfabetis dari A-Z demi kemudahan visualisasi data.

---

## 📊 Analisis Inventori Tambahan
Aplikasi ini dilengkapi fitur kalkulasi otomatis untuk menghitung metrik penting toko:
* Jumlah jenis variasi produk yang tersedia.
* Total keseluruhan kuantitas stok fisik di gudang.
* Total nilai aset investasi inventori (Kalkulasi: Harga $\times$ Stok).
* Deteksi otomatis untuk komoditas dengan stok terbanyak dan tersedikit.
