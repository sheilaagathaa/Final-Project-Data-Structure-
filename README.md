# Final-Project-Data-Structure-
Inventory Management System Built with Python, Featuring CSV Storage, CRUD Operations, Searching, Sorting, Stack, and Queue.
## 👤 Identitas Mahasiswa
* [cite_start]**Nama:** Sheila Syah Agatha [cite: 158]
* [cite_start]**NIM:** 25416255201075 [cite: 159]
* [cite_start]**Kelas:** IF25C [cite: 161]
* [cite_start]**Mata Kuliah:** Struktur Data [cite: 162]

---

## 🚀 Fitur Utama & Operasi CRUD
[cite_start]Aplikasi ini mendukung manajemen data barang secara penuh yang langsung tersinkronisasi secara real-time ke dalam file `barang.csv`[cite: 167]:
1. [cite_start]**Create (Tambah Barang):** Menambahkan data barang baru lengkap dengan validasi ID unik[cite: 183, 189].
2. [cite_start]**Read (Lihat Barang):** Menampilkan seluruh daftar barang dalam bentuk tabel yang rapi di terminal[cite: 193, 201].
3. [cite_start]**Update (Ubah Barang):** Memperbarui informasi barang (Nama, Kategori, Harga, Stok) secara selektif berdasarkan ID[cite: 202, 211].
4. [cite_start]**Delete (Hapus Barang):** Menghapus data barang secara permanen dari sistem basis data[cite: 207, 218].

---

## 🧠 Implementasi Struktur Data & Algoritma
Sesuai dengan persyaratan teknis wajib, aplikasi ini mengimplementasikan konsep struktur data murni demi mengoptimalkan pemrosesan data:

### 1. Hash Map / Dictionary
[cite_start]Digunakan sebagai struktur penyimpanan basis data utama di dalam program (`data_base = {}`)[cite: 192]. Dengan memanfaatkan konsep *Key-Value pair* di mana `ID Barang` bertindak sebagai *key* unik, proses pencarian, pembaruan, dan penghapusan data dapat diakses dengan efisiensi waktu yang optimal.

### 2. Queue (Antrean Custom)
[cite_start]Dibuat melalui struktur kelas mandiri untuk menangani **Sistem Antrean Restock Otomatis**[cite: 280]. [cite_start]Ketika transaksi barang keluar menyebabkan sisa stok berada di bawah batas minimum ($\le 5$), ID barang tersebut akan otomatis dimasukkan ke dalam antrean berprinsip *First-In, First-Out* (FIFO) untuk diprioritaskan pada menu proses restock[cite: 294, 296].

### 3. Searching (Sequential Search)
[cite_start]Mekanisme pencarian fleksibel pada menu "Cari Barang", di mana pengguna dapat melacak item berdasarkan kecocokan ID maupun potongan kata dari nama barang secara dinamis[cite: 221, 228].

### 4. Sorting (Bubble Sort)
[cite_start]Mengimplementasikan algoritma pengurutan Bubble Sort secara manual untuk dua kebutuhan analisis data yang berbeda[cite: 255]:
* [cite_start]**Urutkan Stok:** Mengurutkan barang dari jumlah stok terkecil (skenario prioritas pengadaan kembali)[cite: 263, 266].
* [cite_start]**Urutkan Nama:** Mengurutkan nama barang secara alfabetis dari A-Z demi kemudahan visualisasi data[cite: 265, 268].

---

## 📊 Analisis Inventori Tambahan
[cite_start]Aplikasi ini dilengkapi fitur kalkulasi otomatis untuk menghitung metrik penting toko[cite: 297]:
* [cite_start]Jumlah jenis variasi produk yang tersedia[cite: 302].
* [cite_start]Total keseluruhan kuantitas stok fisik di gudang[cite: 304].
* [cite_start]Total nilai aset investasi inventori (Kalkulasi: Harga $\times$ Stok)[cite: 306].
* [cite_start]Deteksi otomatis untuk komoditas dengan stok terbanyak dan tersedikit[cite: 307, 309].
