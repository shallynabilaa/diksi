"""
Seed database dengan data DIKSI 1501 BPS Kabupaten Kerinci.
Jalankan: python seed.py
"""
from database import engine, SessionLocal, Base
import models

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    try:
        # ── KEPENDUDUKAN ──────────────────────────────────────────
        if db.query(models.Kependudukan).count() == 0:
            data = [
                models.Kependudukan(tahun=2019, jumlah_penduduk=255.8,  laju_pertumbuhan=1.07, kepadatan=69.6, pct_usia_0_14=22.1, pct_usia_15_59=63.8, pct_usia_60_plus=14.1, rasio_jenis_kelamin=101),
                models.Kependudukan(tahun=2020, jumlah_penduduk=259.4,  laju_pertumbuhan=1.41, kepadatan=70.6, pct_usia_0_14=21.8, pct_usia_15_59=64.0, pct_usia_60_plus=14.2, rasio_jenis_kelamin=101),
                models.Kependudukan(tahun=2021, jumlah_penduduk=262.7,  laju_pertumbuhan=1.27, kepadatan=71.5, pct_usia_0_14=21.5, pct_usia_15_59=64.1, pct_usia_60_plus=14.4, rasio_jenis_kelamin=102),
                models.Kependudukan(tahun=2022, jumlah_penduduk=265.3,  laju_pertumbuhan=0.99, kepadatan=72.2, pct_usia_0_14=21.2, pct_usia_15_59=64.2, pct_usia_60_plus=14.6, rasio_jenis_kelamin=102),
                models.Kependudukan(tahun=2023, jumlah_penduduk=268.1,  laju_pertumbuhan=1.05, kepadatan=73.0, pct_usia_0_14=21.0, pct_usia_15_59=64.3, pct_usia_60_plus=14.7, rasio_jenis_kelamin=102),
                models.Kependudukan(tahun=2024, jumlah_penduduk=270.58, laju_pertumbuhan=0.92, kepadatan=73.6, pct_usia_0_14=20.93, pct_usia_15_59=64.28, pct_usia_60_plus=14.79, rasio_jenis_kelamin=102),
            ]
            db.add_all(data)

        # ── KETENAGAKERJAAN ───────────────────────────────────────
        if db.query(models.Ketenagakerjaan).count() == 0:
            data = [
                models.Ketenagakerjaan(tahun=2019, tpt=4.21, tpak=70.1, pct_formal=29.2, pct_informal=70.8, pct_pertanian=57.2, pct_perdagangan=13.4, pct_konstruksi=5.9, pct_pemerintahan=9.1, pct_lainnya=14.4),
                models.Ketenagakerjaan(tahun=2020, tpt=4.68, tpak=69.8, pct_formal=28.5, pct_informal=71.5, pct_pertanian=58.1, pct_perdagangan=13.1, pct_konstruksi=5.7, pct_pemerintahan=8.9, pct_lainnya=14.2),
                models.Ketenagakerjaan(tahun=2021, tpt=3.87, tpak=70.4, pct_formal=29.8, pct_informal=70.2, pct_pertanian=57.0, pct_perdagangan=13.5, pct_konstruksi=6.1, pct_pemerintahan=9.2, pct_lainnya=14.2),
                models.Ketenagakerjaan(tahun=2022, tpt=3.45, tpak=71.2, pct_formal=30.5, pct_informal=69.5, pct_pertanian=56.4, pct_perdagangan=13.8, pct_konstruksi=6.4, pct_pemerintahan=9.3, pct_lainnya=14.1),
                models.Ketenagakerjaan(tahun=2023, tpt=3.28, tpak=71.8, pct_formal=31.2, pct_informal=68.8, pct_pertanian=55.8, pct_perdagangan=14.0, pct_konstruksi=6.6, pct_pemerintahan=9.4, pct_lainnya=14.2),
                models.Ketenagakerjaan(tahun=2024, tpt=3.12, tpak=72.4, pct_formal=31.8, pct_informal=68.2, pct_pertanian=55.4, pct_perdagangan=14.2, pct_konstruksi=6.8, pct_pemerintahan=9.5, pct_lainnya=14.1),
            ]
            db.add_all(data)

        # ── KEMISKINAN ────────────────────────────────────────────
        if db.query(models.Kemiskinan).count() == 0:
            data = [
                models.Kemiskinan(tahun=2019, pct_miskin=8.82, jumlah_miskin=22.51, garis_kemiskinan=418000, gini_ratio=0.298, p1_kedalaman=1.42, p2_keparahan=0.35, pct_gk_makanan=75.2, pct_gk_nonmakanan=24.8),
                models.Kemiskinan(tahun=2020, pct_miskin=8.41, jumlah_miskin=21.78, garis_kemiskinan=431000, gini_ratio=0.294, p1_kedalaman=1.38, p2_keparahan=0.33, pct_gk_makanan=75.0, pct_gk_nonmakanan=25.0),
                models.Kemiskinan(tahun=2021, pct_miskin=8.15, jumlah_miskin=21.41, garis_kemiskinan=451000, gini_ratio=0.291, p1_kedalaman=1.35, p2_keparahan=0.32, pct_gk_makanan=74.8, pct_gk_nonmakanan=25.2),
                models.Kemiskinan(tahun=2022, pct_miskin=7.89, jumlah_miskin=20.93, garis_kemiskinan=473000, gini_ratio=0.291, p1_kedalaman=1.32, p2_keparahan=0.31, pct_gk_makanan=74.6, pct_gk_nonmakanan=25.4),
                models.Kemiskinan(tahun=2023, pct_miskin=7.72, jumlah_miskin=20.68, garis_kemiskinan=510000, gini_ratio=0.287, p1_kedalaman=1.24, p2_keparahan=0.28, pct_gk_makanan=74.4, pct_gk_nonmakanan=25.6),
                models.Kemiskinan(tahun=2024, pct_miskin=7.48, jumlah_miskin=20.24, garis_kemiskinan=542000, gini_ratio=0.284, p1_kedalaman=1.18, p2_keparahan=0.25, pct_gk_makanan=74.3, pct_gk_nonmakanan=25.7),
            ]
            db.add_all(data)

        # ── IPM ───────────────────────────────────────────────────
        if db.query(models.IPM).count() == 0:
            data = [
                models.IPM(tahun=2019, nilai_ipm=69.74, ahh=69.82, hls=12.48, rls=7.98,  pengeluaran_perkapita=9.8),
                models.IPM(tahun=2020, nilai_ipm=70.02, ahh=70.05, hls=12.61, rls=8.10,  pengeluaran_perkapita=10.0),
                models.IPM(tahun=2021, nilai_ipm=70.31, ahh=70.24, hls=12.70, rls=8.22,  pengeluaran_perkapita=10.3),
                models.IPM(tahun=2022, nilai_ipm=70.85, ahh=70.48, hls=12.79, rls=8.35,  pengeluaran_perkapita=10.7),
                models.IPM(tahun=2023, nilai_ipm=71.39, ahh=70.74, hls=12.86, rls=8.47,  pengeluaran_perkapita=11.2),
            ]
            db.add_all(data)

        # ── PDRB ──────────────────────────────────────────────────
        if db.query(models.PDRB).count() == 0:
            data = [
                models.PDRB(tahun=2019, pdrb_adhb=9.82,  pdrb_adhk=7.21, pdrb_perkapita=38.4, lpe=5.01,  pct_pertanian=49.80, pct_perdagangan=11.80, pct_konstruksi=8.20, pct_pemerintahan=7.60, pct_lainnya=22.60),
                models.PDRB(tahun=2020, pdrb_adhb=9.71,  pdrb_adhk=7.12, pdrb_perkapita=37.2, lpe=-1.23, pct_pertanian=50.20, pct_perdagangan=11.50, pct_konstruksi=7.90, pct_pemerintahan=7.80, pct_lainnya=22.60),
                models.PDRB(tahun=2021, pdrb_adhb=10.24, pdrb_adhk=7.39, pdrb_perkapita=39.5, lpe=3.82,  pct_pertanian=49.90, pct_perdagangan=11.90, pct_konstruksi=8.10, pct_pemerintahan=7.70, pct_lainnya=22.40),
                models.PDRB(tahun=2022, pdrb_adhb=11.58, pdrb_adhk=7.79, pdrb_perkapita=44.8, lpe=5.41,  pct_pertanian=49.20, pct_perdagangan=12.10, pct_konstruksi=9.00, pct_pemerintahan=7.80, pct_lainnya=21.90),
                models.PDRB(tahun=2023, pdrb_adhb=13.40, pdrb_adhk=8.24, pdrb_perkapita=52.4, lpe=5.73,  pct_pertanian=48.28, pct_perdagangan=12.40, pct_konstruksi=9.60, pct_pemerintahan=7.80, pct_lainnya=21.92),
            ]
            db.add_all(data)

        # ── INFLASI ───────────────────────────────────────────────
        if db.query(models.Inflasi).count() == 0:
            bulan_names = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
            mtm_2024 = [0.42, 0.31, 0.55, 0.28, 0.17, 0.38, -0.99, 0.22, 0.15, 0.44, 0.29, 0.33]
            yoy_2024 = [4.12, 3.98, 3.87, 3.72, 3.58, 3.52, 3.46, 3.38, 3.31, 3.24, 3.19, 3.15]
            ytd_2024 = [0.42, 0.73, 1.28, 1.56, 1.73, 2.11, 1.67, 1.89, 2.04, 2.48, 2.77, 3.15]
            ihk_2024  = [103.91, 104.23, 104.80, 105.09, 105.27, 105.67, 104.63, 104.86, 105.02, 105.48, 105.79, 106.14]

            for i in range(12):
                db.add(models.Inflasi(
                    tahun=2024, bulan=i+1, nama_bulan=bulan_names[i],
                    inflasi_mtm=mtm_2024[i], inflasi_yoy=yoy_2024[i],
                    inflasi_ytd=ytd_2024[i], ihk=ihk_2024[i]
                ))

        # ── KOMPONEN INFLASI Juli 2024 ─────────────────────────────
        if db.query(models.KomponenInflasi).count() == 0:
            komponen = [
                ("Makanan, Minuman & Tembakau",           1.82),
                ("Perumahan, Air, Listrik & Gas",          0.74),
                ("Kesehatan",                              0.38),
                ("Transportasi",                           0.29),
                ("Pendidikan",                             0.15),
                ("Pakaian & Alas Kaki",                   0.08),
                ("Perlengkapan Rumah Tangga",              0.06),
                ("Rekreasi, Olahraga & Budaya",            0.02),
                ("Restoran & Hotel",                       0.02),
                ("Informasi, Komunikasi & Jasa Keuangan", -0.56),
            ]
            for nama, andil in komponen:
                db.add(models.KomponenInflasi(tahun=2024, bulan=7, kelompok=nama, andil=andil))

        db.commit()
        print("✅ Seed berhasil! Database siap digunakan.")

    except Exception as e:
        db.rollback()
        print(f"❌ Error saat seeding: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
