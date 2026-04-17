from sqlalchemy import create_engine, Column, Integer, String, Date, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime, date

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'Doctors'
    Doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    Full_name = Column(String(255), nullable=False)
    Specialization = Column(String(255), nullable=False)
    Account = Column(String(255), unique=True, nullable=False)
    Password = Column(String(255), nullable=False)
    Phone = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

class Patient(Base):
    __tablename__ = 'Patients'
    Patient_id = Column(Integer, primary_key=True, autoincrement=True)
    Full_name = Column(String(255), nullable=False)
    Dob = Column(Date)
    Gender = Column(String(10), nullable=False)
    Phone = Column(String(20))
    Address = Column(Text)
    created_at = Column(DateTime, default=datetime.now)

class MedicalRecord(Base):
    __tablename__ = 'MedicalRecords'
    Record_id = Column(Integer, primary_key=True, autoincrement=True)
    Patient_id = Column(Integer, ForeignKey('Patients.Patient_id'), nullable=False)
    Doctor_id = Column(Integer, ForeignKey('Doctors.Doctor_id'), nullable=False)
    Visit_date = Column(Date, default=datetime.now)
    Symptoms = Column(Text)
    Diagnosis = Column(Text)
    Treatment = Column(Text)
    Notes = Column(Text) 
    Status = Column(String(50), default='Chờ khám')
    created_at = Column(DateTime, default=datetime.now)
    
    patient = relationship("Patient")
    doctor = relationship("Doctor")

# KẾT NỐI CSDL SQLITE
engine = create_engine('sqlite:///hospital.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# TỰ ĐỘNG TẠO BẢNG NẾU FILE CHƯA TỒN TẠI
Base.metadata.create_all(bind=engine)

# KHỞI TẠO DỮ LIỆU MẪU (DUMMY DATA) CHO LẦN ĐẦU CHẠY
session = SessionLocal()
if session.query(Doctor).count() == 0:
    
    # 1. Thêm 3 Bác sĩ
    docs = [
        Doctor(Full_name="Vũ Thanh Tùng", Specialization="Đa Khoa", Account="tung_bs", Password="1", Phone="0393056656"),
        Doctor(Full_name="Trần Văn Trung", Specialization="Nhi Khoa", Account="bs_trung", Password="1", Phone="0911222333"),
        Doctor(Full_name="Đặng Minh Tân", Specialization="Da Liễu", Account="bs_tan", Password="1", Phone="0944555666")
    ]
    session.add_all(docs)
    
    # 2. Thêm 10 Bệnh nhân mẫu
    patients = [
        Patient(Full_name="Nguyễn Văn An", Dob=date(1990, 5, 15), Gender="Nam", Phone="0901234567", Address="Ba Đình, Hà Nội"),
        Patient(Full_name="Trần Thị Bình", Dob=date(1985, 10, 22), Gender="Nữ", Phone="0912345678", Address="Cầu Giấy, Hà Nội"),
        Patient(Full_name="Lê Văn Cường", Dob=date(2000, 1, 10), Gender="Nam", Phone="0923456789", Address="Đống Đa, Hà Nội"),
        Patient(Full_name="Phạm Thị Dung", Dob=date(1992, 8, 30), Gender="Nữ", Phone="0934567890", Address="Thanh Xuân, Hà Nội"),
        Patient(Full_name="Hoàng Văn Em", Dob=date(1988, 12, 5), Gender="Nam", Phone="0945678901", Address="Hai Bà Trưng, Hà Nội"),
        Patient(Full_name="Vũ Thị Phương", Dob=date(1995, 4, 18), Gender="Nữ", Phone="0956789012", Address="Hoàng Mai, Hà Nội"),
        Patient(Full_name="Đỗ Văn Giang", Dob=date(1980, 7, 25), Gender="Nam", Phone="0967890123", Address="Tây Hồ, Hà Nội"),
        Patient(Full_name="Bùi Thị Hoa", Dob=date(2005, 11, 11), Gender="Nữ", Phone="0978901234", Address="Nam Từ Liêm, Hà Nội"),
        Patient(Full_name="Ngô Văn Ích", Dob=date(1998, 2, 14), Gender="Nam", Phone="0989012345", Address="Bắc Từ Liêm, Hà Nội"),
        Patient(Full_name="Đinh Thị Kiều", Dob=date(1993, 9, 9), Gender="Nữ", Phone="0990123456", Address="Hà Đông, Hà Nội")
    ]
    session.add_all(patients)
    
    session.commit()
session.close()