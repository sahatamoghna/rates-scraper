from xescraper.models import Session, XeConversion
import re

def _to_float(s):
    """Safe string->float for values like '1,234.5678' or '1 234.5678'."""
    if s is None:
        return None
    txt = str(s).strip()
    if not txt:
        return None
    # Remove commas/spaces; keep dot
    txt = re.sub(r"[,\s]", "", txt)
    try:
        return float(txt)
    except Exception:
        return None

class MySQLPipeline:
    def open_spider(self, spider):
        self.session = Session()
        spider.logger.info("MySQL database session opened.")

    def close_spider(self, spider):
        self.session.close()
        spider.logger.info("MySQL database session closed.")

    def process_item(self, item, spider):
        # We only expect USD rows to reach here (spider filters),
        # but let's be defensive.
        currency = (item.get("currency") or "").upper()
        if currency != "USD":
            spider.logger.debug(f"Skipping non-USD row: {item}")
            return item

        source = (item.get("source_country") or "").upper()
        date = item.get("date")
        rate = _to_float(item.get("rate"))
        inv  = _to_float(item.get("inverse_rate"))

        rec_id = f"{source}_{date}_USD"

        try:
            record = XeConversion(
                id=rec_id,
                source_country=source,
                date=date,
                currency="USD",
                rate=rate,
                inverse_rate=inv
            )
            # merge = insert or update on PK conflict
            self.session.merge(record)
            self.session.commit()
            spider.logger.info(f"✅ Upserted xe_conversions: {record.id}")
        except Exception as e:
            self.session.rollback()
            spider.logger.error(f"❌ Error saving xe_conversions record ({rec_id}): {e}")

        return item
