# DIKSI 1501 — Dashboard Statistik BPS Kabupaten Kerinci

Stack: **FastAPI** (Python) + **MySQL** + **HTML/CSS/JS**

## Struktur Proyek

```
diksi1501/
├── backend/
│   ├── main.py          # FastAPI app & semua route API
│   ├── database.py      # Koneksi MySQL & ORM SQLAlchemy
│   ├── models.py        # Model tabel database
│   ├── schemas.py       # Pydantic schemas (validasi data)
│   ├── crud.py          # Fungsi baca/tulis database
│   ├── seed.py          # Isi database dengan data awal
│   └── requirements.txt
├── frontend/
│   ├── index.html       # Halaman utama dashboard
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       ├── api.js   # Fetch data dari backend
│   │       ├── charts.js # Render semua grafik Chart.js
│   │       └── app.js   # Logic navigasi & UI
└── README.md
```

## Cara Menjalankan

### 1. Setup Database MySQL
```sql
CREATE DATABASE diksi1501 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'diksi_user'@'localhost' IDENTIFIED BY 'diksi_pass123';
GRANT ALL PRIVILEGES ON diksi1501.* TO 'diksi_user'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Konfigurasi Environment
Buat file `.env` di folder `backend/`:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=diksi1501
DB_USER=diksi_user
DB_PASS=diksi_pass123
```

### 4. Inisialisasi & Seed Database
```bash
cd backend
python seed.py
```

### 5. Jalankan Backend
```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 6. Buka Frontend
Buka `frontend/index.html` di browser, atau serve dengan:
```bash
cd frontend
python -m http.server 5500
# Buka http://localhost:5500
```

## API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/api/ringkasan` | Semua indikator ringkasan |
| GET | `/api/kependudukan` | Data kependudukan |
| GET | `/api/kependudukan/tren` | Tren penduduk per tahun |
| GET | `/api/ketenagakerjaan` | Data ketenagakerjaan |
| GET | `/api/ketenagakerjaan/tren` | Tren TPT per tahun |
| GET | `/api/kemiskinan` | Data kemiskinan |
| GET | `/api/kemiskinan/tren` | Tren kemiskinan per tahun |
| GET | `/api/ipm` | Data IPM |
| GET | `/api/ipm/tren` | Tren IPM per tahun |
| GET | `/api/pdrb` | Data PDRB |
| GET | `/api/pdrb/tren` | Tren PDRB per tahun |
| GET | `/api/inflasi` | Data inflasi |
| GET | `/api/inflasi/bulanan` | Inflasi bulanan 2024 |
| GET | `/docs` | Swagger UI (dokumentasi API otomatis) |
