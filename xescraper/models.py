from sqlalchemy import Column, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# New, focused table for the 4 pairs: <source>/USD
class XeConversion(Base):
    __tablename__ = 'xe_conversions'

    # composite key packed into a single id string for simplicity
    id = Column(String(255), primary_key=True)  # e.g., "GBP_2025-08-24_USD"
    source_country = Column(String(10), nullable=False)  # GBP, AUD, EUR, CAD
    date = Column(Date, nullable=False)
    currency = Column(String(10), nullable=False)        # always 'USD'
    rate = Column(Float)                                 # source -> USD
    inverse_rate = Column(Float)                         # USD -> source

# You can keep your old xe_raw_data table if you still want it, but for this request we only
# define and write to xe_conversions. If you still need XeRawData, you can re-add it here.

# Update this to your connection as needed
DATABASE_URL = 'mysql+pymysql://root:rio1005@localhost:3306/xe_data'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
