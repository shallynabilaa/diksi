from sqlalchemy import Column, Integer, Float, String, SmallInteger
from database import Base


class Kependudukan(Base):
    __tablename__ = "kependudukan"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False, unique=True)
    jumlah_penduduk = Column(Float, comment="ribu jiwa")
    laju_pertumbuhan = Column(Float, comment="persen per tahun")
    kepadatan = Column(Float, comment="jiwa per km2")
    pct_usia_0_14 = Column(Float, comment="persen")
    pct_usia_15_59 = Column(Float, comment="persen")
    pct_usia_60_plus = Column(Float, comment="persen")
    rasio_jenis_kelamin = Column(Float, comment="laki per 100 perempuan")


class Ketenagakerjaan(Base):
    __tablename__ = "ketenagakerjaan"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False, unique=True)
    tpt = Column(Float, comment="Tingkat Pengangguran Terbuka persen")
    tpak = Column(Float, comment="Tingkat Partisipasi Angkatan Kerja persen")
    pct_formal = Column(Float, comment="persen pekerja formal")
    pct_informal = Column(Float, comment="persen pekerja informal")
    pct_pertanian = Column(Float, comment="persen di sektor pertanian")
    pct_perdagangan = Column(Float, comment="persen di sektor perdagangan")
    pct_konstruksi = Column(Float, comment="persen di sektor konstruksi")
    pct_pemerintahan = Column(Float, comment="persen di sektor pemerintahan")
    pct_lainnya = Column(Float, comment="persen di sektor lainnya")


class Kemiskinan(Base):
    __tablename__ = "kemiskinan"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False, unique=True)
    pct_miskin = Column(Float, comment="persen penduduk miskin")
    jumlah_miskin = Column(Float, comment="ribu jiwa")
    garis_kemiskinan = Column(Integer, comment="rupiah per kapita per bulan")
    gini_ratio = Column(Float)
    p1_kedalaman = Column(Float, comment="indeks kedalaman kemiskinan")
    p2_keparahan = Column(Float, comment="indeks keparahan kemiskinan")
    pct_gk_makanan = Column(Float, comment="persen komponen makanan")
    pct_gk_nonmakanan = Column(Float, comment="persen komponen non-makanan")


class IPM(Base):
    __tablename__ = "ipm"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False, unique=True)
    nilai_ipm = Column(Float, comment="nilai IPM")
    ahh = Column(Float, comment="Angka Harapan Hidup tahun")
    hls = Column(Float, comment="Harapan Lama Sekolah tahun")
    rls = Column(Float, comment="Rata-rata Lama Sekolah tahun")
    pengeluaran_perkapita = Column(Float, comment="juta rupiah per tahun")


class PDRB(Base):
    __tablename__ = "pdrb"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False, unique=True)
    pdrb_adhb = Column(Float, comment="triliun rupiah harga berlaku")
    pdrb_adhk = Column(Float, comment="triliun rupiah harga konstan 2010")
    pdrb_perkapita = Column(Float, comment="juta rupiah per tahun")
    lpe = Column(Float, comment="laju pertumbuhan ekonomi persen")
    pct_pertanian = Column(Float, comment="persen kontribusi pertanian")
    pct_perdagangan = Column(Float, comment="persen kontribusi perdagangan")
    pct_konstruksi = Column(Float, comment="persen kontribusi konstruksi")
    pct_pemerintahan = Column(Float, comment="persen kontribusi pemerintahan")
    pct_lainnya = Column(Float, comment="persen kontribusi sektor lain")


class Inflasi(Base):
    __tablename__ = "inflasi"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False)
    bulan = Column(SmallInteger, nullable=False, comment="1-12")
    nama_bulan = Column(String(15))
    inflasi_mtm = Column(Float, comment="inflasi month to month persen")
    inflasi_yoy = Column(Float, comment="inflasi year on year persen")
    inflasi_ytd = Column(Float, comment="inflasi year to date persen")
    ihk = Column(Float, comment="Indeks Harga Konsumen")


class KomponenInflasi(Base):
    __tablename__ = "komponen_inflasi"
    id = Column(Integer, primary_key=True, index=True)
    tahun = Column(SmallInteger, nullable=False)
    bulan = Column(SmallInteger, nullable=False)
    kelompok = Column(String(80), nullable=False)
    andil = Column(Float, comment="andil terhadap inflasi yoy persen")
