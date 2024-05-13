![gamabr](https://github.com/lahadiyani/WatchMan/blob/main/Screenshot%20(42).png)

# Alat Forensik untuk OSINT

Alat ini menyediakan fungsionalitas untuk pengumpulan Open Source Intelligence (OSINT). Ini mencakup fitur-fitur untuk mencari informasi tentang seseorang berdasarkan nama atau gambar.

## Impor Modul

- `requests` untuk membuat permintaan HTTP
- `os`, `time`, `re`, `random`, `json` untuk berbagai utilitas
- `rich` untuk output konsol berwarna
- `bs4` (Beautiful Soup) untuk parsing HTML
- `serpapi` untuk berinteraksi dengan API pencarian Google

## Fungsi

### 1. `google_search(query)`

Fungsi ini melakukan pencarian Google untuk kueri yang diberikan dan mengembalikan hasil pencarian.

### 2. `bing_search(query)`

Sama seperti `google_search`, fungsi ini melakukan pencarian Bing untuk kueri yang diberikan dan mengembalikan hasil pencarian.

### 3. `cari_person(query, se="google")`

Fungsi ini memungkinkan pencarian seseorang menggunakan mesin pencari Google atau Bing berdasarkan kueri yang ditentukan.

### 4. `person()`

Fungsi ini menyediakan antarmuka interaktif untuk mencari informasi tentang seseorang. Ini meminta pengguna untuk memasukkan kueri pencarian dan memilih mesin pencari (Google/Bing).

### 5. `img_person()`

Memungkinkan pencarian informasi tentang seseorang menggunakan gambar mereka. Ini meminta pengguna untuk memasukkan jalur/URL gambar dan menggunakan API Pencarian Gambar Terbalik Google untuk mendapatkan informasi yang relevan.

### 6. `banner()`

Mencetak banner dengan nama alat dan informasi penulis.

### 7. `menu()`

Menampilkan menu untuk memilih berbagai fungsionalitas yang disediakan oleh alat.

## Penggunaan

Untuk menggunakan alat ini, cukup jalankan skripnya. Ini akan menampilkan menu di mana Anda dapat memilih antara mencari seseorang berdasarkan nama atau gambar.

## Persyaratan

- Python 3.x
- requirement yang tercantum di `import module`
- Kunci API untuk Pencarian Gambar Terbalik Google (ganti `"Your Api Key"` dalam fungsi `img_person()` dengan kunci API sesungguhnya Anda)
- cookie anda bisa mencari nya dengan inspect elemen ke chrome google 

## info

Alat ini disediakan hanya untuk tujuan pendidikan dan informasi. Penulis tidak bertanggung jawab atas penyalahgunaan atau kegiatan ilegal yang dilakukan menggunakan alat ini.

## Penulis

Dibuat oleh Hadi dan contributor.


login di https://serpapi.com/users/sign_in untuk mendapatkan apikey
untuk cookie tinggal inspect elemen pas nyari di google
