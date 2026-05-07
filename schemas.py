from pydantic import BaseModel
from typing import List, Optional


class KependudukanSchema(BaseModel):
    tahun: int
    jumlah_penduduk: float
    laju_pertumbuhan: Optional[float]
    kepadatan: Optional[float]
    pct_usia_0_14: Optional[float]
    pct_usia_15_59: Optional[float]
    pct_usia_60_plus: Optional[float]
    rasio_jenis_kelamin: Optional[float]

    class Config:
        from_attributes = True


class KetenagakerjaanSchema(BaseModel):
    tahun: int
    tpt: float
    tpak: Optional[float]
    pct_formal: Optional[float]
    pct_informal: Optional[float]
    pct_pertanian: Optional[float]
    pct_perdagangan: Optional[float]
    pct_konstruksi: Optional[float]
    pct_pemerintahan: Optional[float]
    pct_lainnya: Optional[float]

    class Config:
        from_attributes = True


class KemiskinanSchema(BaseModel):
    tahun: int
    pct_miskin: float
    jumlah_miskin: Optional[float]
    garis_kemiskinan: Optional[int]
    gini_ratio: Optional[float]
    p1_kedalaman: Optional[float]
    p2_keparahan: Optional[float]
    pct_gk_makanan: Optional[float]
    pct_gk_nonmakanan: Optional[float]

    class Config:
        from_attributes = True


class IPMSchema(BaseModel):
    tahun: int
    nilai_ipm: float
    ahh: Optional[float]
    hls: Optional[float]
    rls: Optional[float]
    pengeluaran_perkapita: Optional[float]

    class Config:
        from_attributes = True


class PDRBSchema(BaseModel):
    tahun: int
    pdrb_adhb: float
    pdrb_adhk: Optional[float]
    pdrb_perkapita: Optional[float]
    lpe: Optional[float]
    pct_pertanian: Optional[float]
    pct_perdagangan: Optional[float]
    pct_konstruksi: Optional[float]
    pct_pemerintahan: Optional[float]
    pct_lainnya: Optional[float]

    class Config:
        from_attributes = True


class InflasiSchema(BaseModel):
    tahun: int
    bulan: int
    nama_bulan: Optional[str]
    inflasi_mtm: Optional[float]
    inflasi_yoy: Optional[float]
    inflasi_ytd: Optional[float]
    ihk: Optional[float]

    class Config:
        from_attributes = True


class KomponenInflasiSchema(BaseModel):
    tahun: int
    bulan: int
    kelompok: str
    andil: float

    class Config:
        from_attributes = True


class RingkasanSchema(BaseModel):
    jumlah_penduduk: float
    laju_pertumbuhan_penduduk: float
    tpt: float
    tpak: float
    pct_miskin: float
    garis_kemiskinan: int
    ipm: float
    ahh: float
    pdrb_adhb: float
    lpe: float
    pdrb_perkapita: float
    inflasi_yoy: float
    inflasi_mtm: float
    ihk: float
