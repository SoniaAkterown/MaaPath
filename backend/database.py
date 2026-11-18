import os
from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dotenv import load_dotenv

load_dotenv()

# লোকালি SQLite, প্রোডাকশনে .env এ DATABASE_URL দিলে PostgreSQL চলবে
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./maapath.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Mother(Base):
    __tablename__ = "mothers"

    id = Column(String(32), primary_key=True, index=True)  # e.g., MP-BD-2409
    name = Column(String(120), nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String(30), nullable=False)
    guardian_phone = Column(String(30), nullable=True)
    address = Column(String(255), nullable=False)
    lmp = Column(String(20), nullable=False)               # YYYY-MM-DD
    edd = Column(String(30), nullable=False)
    gestational_week = Column(Integer, default=1)
    blood_group = Column(String(10), default="O+")
    prev_history = Column(String(120), default="First Pregnancy")
    diseases = Column(String(255), default="None")
    medications = Column(String(255), default="IFA, Calcium")
    risk_level = Column(String(30), default="Low")
    created_at = Column(DateTime, default=datetime.utcnow)

    vitals = relationship("VitalLog", back_populates="mother", cascade="all, delete-orphan")
    anc_visits = relationship("ANCVisit", back_populates="mother", cascade="all, delete-orphan")
    referrals = relationship("Referral", back_populates="mother", cascade="all, delete-orphan")


class VitalLog(Base):
    __tablename__ = "vital_logs"

    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(String(32), ForeignKey("mothers.id"), nullable=False)
    date = Column(String(30), nullable=False)
    week = Column(String(10), nullable=False)
    bp = Column(String(20), nullable=False)
    weight = Column(String(20), nullable=False)
    sugar = Column(String(20), default="5.2 mmol/L")
    hb = Column(String(20), default="11.5 g/dL")
    status = Column(String(20), default="Normal")
    created_at = Column(DateTime, default=datetime.utcnow)

    mother = relationship("Mother", back_populates="vitals")


class ANCVisit(Base):
    __tablename__ = "anc_visits"

    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(String(32), ForeignKey("mothers.id"), nullable=False)
    title = Column(String(120), nullable=False)
    scheduled_date = Column(String(30), nullable=False)
    facility = Column(String(150), default="Savar Upazila Health Complex")
    notes = Column(Text, default="")
    status = Column(String(20), default="upcoming")  # upcoming | completed | missed

    mother = relationship("Mother", back_populates="anc_visits")


class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(String(32), ForeignKey("mothers.id"), nullable=False)
    hospital_name = Column(String(150), nullable=False)
    urgency = Column(String(30), default="High")
    reason = Column(Text, nullable=False)
    status = Column(String(40), default="Dispatched & Notified")
    created_at = Column(DateTime, default=datetime.utcnow)

    mother = relationship("Mother", back_populates="referrals")


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()