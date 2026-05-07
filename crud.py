from sqlalchemy.orm import Session
from sqlalchemy import desc
import models


def get_kependudukan_latest(db: Session):
    return db.query(models.Kependudukan).order_by(desc(models.Kependudukan.tahun)).first()

def get_kependudukan_tren(db: Session):
    return db.query(models.Kependudukan).order_by(models.Kependudukan.tahun).all()


def get_ketenagakerjaan_latest(db: Session):
    return db.query(models.Ketenagakerjaan).order_by(desc(models.Ketenagakerjaan.tahun)).first()

def get_ketenagakerjaan_tren(db: Session):
    return db.query(models.Ketenagakerjaan).order_by(models.Ketenagakerjaan.tahun).all()


def get_kemiskinan_latest(db: Session):
    return db.query(models.Kemiskinan).order_by(desc(models.Kemiskinan.tahun)).first()

def get_kemiskinan_tren(db: Session):
    return db.query(models.Kemiskinan).order_by(models.Kemiskinan.tahun).all()


def get_ipm_latest(db: Session):
    return db.query(models.IPM).order_by(desc(models.IPM.tahun)).first()

def get_ipm_tren(db: Session):
    return db.query(models.IPM).order_by(models.IPM.tahun).all()


def get_pdrb_latest(db: Session):
    return db.query(models.PDRB).order_by(desc(models.PDRB.tahun)).first()

def get_pdrb_tren(db: Session):
    return db.query(models.PDRB).order_by(models.PDRB.tahun).all()


def get_inflasi_latest(db: Session):
    return db.query(models.Inflasi).order_by(
        desc(models.Inflasi.tahun), desc(models.Inflasi.bulan)
    ).first()

def get_inflasi_bulanan(db: Session, tahun: int = 2024):
    return db.query(models.Inflasi).filter(
        models.Inflasi.tahun == tahun
    ).order_by(models.Inflasi.bulan).all()

def get_komponen_inflasi(db: Session, tahun: int = 2024, bulan: int = 7):
    return db.query(models.KomponenInflasi).filter(
        models.KomponenInflasi.tahun == tahun,
        models.KomponenInflasi.bulan == bulan
    ).all()
