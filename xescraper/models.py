from sqlalchemy import Column, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class XeConversion(Base):
    __tablename__ = 'xe_conversions'

    id = Column(String(255), primary_key=True)  # e.g., "GBP_2025-08-24_USD"
    source_country = Column(String(10), nullable=False)  # GBP, AUD, EUR, CAD
    date = Column(Date, nullable=False)
    currency = Column(String(10), nullable=False)        # always 'USD'
    rate = Column(Float)                                 # source -> USD
    inverse_rate = Column(Float)                         # USD -> source

DATABASE_URL = 'mysql+pymysql://root:rio1005@localhost:3306/xe_data'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
