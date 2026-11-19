import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./maapath.db")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Mother(Base):
    __tablename__ = "mothers"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)
    guardian_phone = Column(String, nullable=True)
    address = Column(String, nullable=False)
    lmp = Column(String, nullable=False)
    edd = Column(String, nullable=False)
    pregnancy_week = Column(Integer, default=1)
    blood_group = Column(String, nullable=False)
    prev_history = Column(String, nullable=True)
    diseases = Column(String, default="None")
    medications = Column(String, default="IFA, Calcium")
    risk_level = Column(String, default="Low")
    created_at = Column(DateTime, default=datetime.utcnow)

class VitalLog(Base):
    __tablename__ = "vitals"
    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(String, ForeignKey("mothers.id"))
    date = Column(String, default=lambda: datetime.now().strftime("%d %b %Y"))
    week = Column(String, nullable=True)
    bp = Column(String, nullable=True)
    weight = Column(String, nullable=True)
    sugar = Column(String, nullable=True)
    hb = Column(String, nullable=True)
    status = Column(String, default="Normal")

class ANCVisit(Base):
    __tablename__ = "anc_visits"
    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(String, ForeignKey("mothers.id"))
    visit_number = Column(Integer, default=1)
    title = Column(String, nullable=True)
    scheduled_date = Column(String, nullable=True)
    location = Column(String, nullable=True)
    status = Column(String, default="upcoming")
    notes = Column(Text, nullable=True)

class Referral(Base):
    __tablename__ = "referrals"
    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(String, ForeignKey("mothers.id"))
    hospital_name = Column(String, nullable=False)
    urgency = Column(String, default="High")
    reason = Column(Text, nullable=True)
    status = Column(String, default="Dispatched")
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
