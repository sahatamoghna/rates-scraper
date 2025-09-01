# XE Currency Rates Scraper

Scrapes historical exchange rates from [XE.com](https://www.xe.com/) for four pairs — **GBP/USD, AUD/USD, CAD/USD, EUR/USD** — and stores them in MySQL. Includes a batch runner for large date ranges and a one-shot export to Excel.

---

## Features
- Daily rates from 2013 to present (configurable date window)
- Focused on four source currencies → USD
- Persists to MySQL table `xe_conversions` via SQLAlchemy
- Month-by-month batch runner with resume support
- Excel export in wide format: `date | GBP/USD | AUD/USD | CAD/USD | EUR/USD`

---

## Stack
- Python 3.9+
- Scrapy, SQLAlchemy, PyMySQL
- pandas, openpyxl
- MySQL 5.7+/8.0+

---

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/rates-scraper.git
cd rates-scraper
pip install -r requirements.txt
````

**Database config**
Set your connection string either in an environment variable:

```bash
set DATABASE_URL=mysql+pymysql://USER:PASSWORD@localhost:3306/xe_data   # Windows
# or
export DATABASE_URL=mysql+pymysql://USER:PASSWORD@localhost:3306/xe_data # macOS/Linux
```

The project defaults to the same URL inside `xescraper/models.py` if the env var is not set.

---

## Usage

### 1) Scrape a single month

```bash
scrapy crawl xe.com -a start=2013-04-01 -a end=2013-04-30 -s LOG_LEVEL=INFO
```

### 2) Scrape a long range (month-by-month)

```bash
python run_batches.py --start 2013-04-01 --end 2025-08-31
```

* Creates a fresh Scrapy process per month (safer for long runs)
* Tracks finished months in `months_done.txt` so you can resume

### 3) Export to Excel

```bash
python export_xe_conversions.py --out xe_conversions.xlsx
```

Outputs a single sheet with columns: `date, GBP/USD, AUD/USD, CAD/USD, EUR/USD`.

---

## Data Model (MySQL)

Table: `xe_conversions`

* `id` (PK): `{SOURCE}_{DATE}_USD` (e.g., `GBP_2013-04-01_USD`)
* `source_country`: `GBP | AUD | CAD | EUR`
* `date`: `DATE`
* `currency`: always `USD`
* `rate`: source → USD (e.g., 1 GBP = X USD)
* `inverse_rate`: USD → source

---

## Project Structure

```
xescraper/
├─ scrapy.cfg
├─ run_batches.py               # Month-by-month runner (resume + retries)
├─ export_xe_conversions.py     # Excel export (wide format)
└─ xescraper/
   ├─ items.py                  # Scrapy items
   ├─ middlewares.py            # (optional) middlewares
   ├─ models.py                 # SQLAlchemy models + engine
   ├─ pipelines.py              # Writes into xe_conversions
   ├─ settings.py               # Scrapy settings (throttling, headers)
   └─ spiders/
      └─ xe_com.py              # XE.com spider (accepts -a start=... -a end=...)
```

---

## Notes

* Uses throttling and respects `robots.txt`
* Missing days will appear blank in Excel (no silent filling)
* Re-running a month upserts rows (safe to repeat)

If you want, I can swap the DB config to **environment-only** (no credentials in code) and add a tiny `.env.example` for extra polish.
```
