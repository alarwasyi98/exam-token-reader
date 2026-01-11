# Pembaca Token Ujian

Aplikasi web sederhana untuk membacakan token ujian secara otomatis menggunakan Web Speech API. Dirancang dengan antarmuka modern minimalis menggunakan prinsip desain Next.js dan ShadCN.

## Deskripsi

Pembaca Token Ujian adalah tools berbasis web yang membantu pengawas ujian atau penyelenggara tes dalam membacakan kode token kepada peserta ujian. Aplikasi ini memanfaatkan teknologi Text-to-Speech (TTS) bawaan browser untuk menghasilkan audio berkualitas tinggi dalam Bahasa Indonesia.

## Fitur Utama

### Kontrol Pembacaan

- **Play & Pause** - Kontrol penuh atas pembacaan audio
- **Resume** - Lanjutkan pembacaan dari posisi terakhir setelah pause
- **Stop** - Hentikan pembacaan kapan saja

### Pengaturan Audio

- **Pemilihan Suara** - Pilih dari berbagai suara Bahasa Indonesia yang tersedia
- **Kecepatan Pembacaan** - Atur kecepatan dari 0.5x hingga 2.0x
- **Test Suara** - Uji coba suara sebelum pembacaan sesungguhnya

### Pengulangan Otomatis

- Pilih jumlah pengulangan dari 1x hingga 5x
- Jeda otomatis 1 detik antar pengulangan
- Status counter real-time menampilkan progress pembacaan

### Antarmuka

- Desain dark mode yang modern dan minimalis
- Grid pattern background dengan radial gradient
- Responsif untuk berbagai ukuran layar
- Komponen form dengan label dan deskripsi yang jelas

## Teknologi

Aplikasi ini dibangun menggunakan teknologi web standar:

- **HTML5** - Struktur markup semantik
- **CSS3** - Styling modern dengan custom properties
- **Vanilla JavaScript** - Logika aplikasi tanpa dependency
- **Web Speech API** - Text-to-Speech synthesis

## Persyaratan Sistem

### Browser yang Didukung

- Google Chrome 33+
- Microsoft Edge 14+
- Safari 7+
- Firefox 49+
- Opera 21+

### Persyaratan Suara

> [!INFO] 
> Untuk hasil terbaik, pastikan Anda telah menginstal paket suara Bahasa Indonesia pada sistem operasi

**Windows:**
1. Buka Settings → Time & Language → Speech
2. Download dan install "Microsoft Gadis" atau suara Indonesia lainnya
3. Restart browser setelah instalasi

**macOS:**
1. Buka System Preferences → Accessibility → Spoken Content
2. Pilih System Voice → Manage Voices
3. Download suara Bahasa Indonesia yang tersedia

**Linux:**
1. Install espeak atau festival dengan paket bahasa Indonesia
2. Konfigurasi melalui speech-dispatcher

## Instalasi

> [!IMPORTANT]
> Pastikan anda telah menginstal [Git](https://git-scm.com) agar dapat menjalankan perintah berikut tanpa masalah

### Clone Repository
```bash
git clone https://github.com/username/pembaca-token-ujian.git
cd pembaca-token-ujian
```

### Jalankan Aplikasi

Tidak memerlukan instalasi dependencies. Cukup buka file HTML di browser:

```bash
# Menggunakan server lokal (recommended)
python -m http.server 8000
# Atau
npx serve

# Atau buka langsung
open index.html  # macOS
start index.html # Windows
xdg-open index.html # Linux
```

Akses aplikasi di `http://localhost:8000`

### Metode Lain (lebih mudah)

* Unduh atau salin keseluruhan kode dalam [index.html](./index.html) dan simpan dalam format html
* Buka file tersebut menggunakan browser yang didudkung.

## Cara Menggunakan

### Langkah Dasar

1. Masukkan token ujian pada kolom input
2. Pilih suara Bahasa Indonesia yang diinginkan
3. Atur kecepatan pembacaan (default: 1.0x)
4. Pilih jumlah pengulangan (default: 1x)
5. Klik tombol "Play" untuk memulai pembacaan

### Tips Penggunaan

- Gunakan tombol "Test" untuk memastikan suara bekerja dengan baik
- Atur kecepatan lebih lambat (0.7x - 0.8x) untuk token yang panjang
- Gunakan pengulangan 2-3x untuk memastikan peserta mencatat dengan benar
- Pause dapat digunakan jika ada gangguan sementara

### Format Token
Token akan dibacakan karakter per karakter dengan jeda. Contoh:

Input: `ABC123`  
Output: "Perhatian, token ujian adalah A B C 1 2 3"

## Struktur Project

```
pembaca-token-ujian/
├── index.html          # File utama aplikasi
├── README.md           # Dokumentasi lengkap
└── .gitignore          # File yang diabaikan Git
```

## Konfigurasi

### Mengubah Delay Antar Pengulangan

Edit nilai timeout di fungsi `bacaTokenBerulang()`:

```javascript
setTimeout(() => {
  if (!isPaused && isPlaying) {
    bacaTokenBerulang(token);
  }
}, 1000); // Ubah nilai 1000 (ms) sesuai kebutuhan
```

### Mengubah Range Kecepatan

Edit atribut pada input range di HTML:

```html
<input type="range" id="rate" min="0.5" max="2" step="0.1" value="1">
```

### Menambah Opsi Pengulangan
Tambahkan tombol baru di section repeat-options:

```html
<button class="repeat-btn" onclick="setRepeat(6)">6x</button>
```

## Batasan dan Keterbatasan

- **Kualitas Suara** - Bergantung pada TTS engine yang tersedia di sistem
- **Dukungan Browser** - Web Speech API tidak didukung di semua browser
- **Koneksi Internet** - Beberapa browser memerlukan koneksi untuk TTS cloud-based
- **Bahasa** - Saat ini hanya mendukung Bahasa Indonesia

## Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/FiturBaru`)
3. Commit perubahan (`git commit -m 'Menambahkan fitur baru'`)
4. Push ke branch (`git push origin feature/FiturBaru`)
5. Buat Pull Request

### Pedoman Kontribusi
- Ikuti style code yang sudah ada
- Tulis commit message yang deskriptif
- Dokumentasikan fitur baru di README
- Test di berbagai browser sebelum submit PR

## Roadmap

Fitur yang direncanakan untuk versi mendatang:

- [ ] Export audio ke file MP3/WAV
- [ ] Preset untuk berbagai jenis token (alfanumerik, numerik, alphabet)
- [ ] Dark/Light mode toggle
- [ ] Keyboard shortcuts
- [ ] History token yang pernah dibacakan
- [ ] Multi-language support
- [ ] PWA (Progressive Web App) support
- [ ] Integrasi dengan Google Cloud Text-to-Speech API

## Troubleshooting

### Suara tidak keluar
- Pastikan volume sistem tidak di-mute
- Cek apakah browser mendukung Web Speech API
- Install paket suara Bahasa Indonesia di sistem operasi
- Coba refresh halaman dan pilih ulang suara

### Tombol Pause tidak berfungsi
- Beberapa browser memiliki implementasi pause yang berbeda
- Gunakan tombol Test untuk menghentikan pembacaan sepenuhnya
- Restart browser jika masalah berlanjut

### Tidak ada suara Bahasa Indonesia
- Install paket bahasa Indonesia dari system settings
- Restart browser setelah instalasi
- Gunakan browser berbeda yang mendukung lebih banyak suara

## Acknowledgments

- Design inspiration: Next.js dan ShadCN UI
- Icons: Unicode emoji characters
- Font: System UI font stack
- TTS Engine: Web Speech API (browser native)

---

**Made with ❤️ for education purposes**
