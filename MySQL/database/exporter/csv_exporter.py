import csv
from .base_exporter import BaseExporter
from utils.logger import logger

class CSVExporter(BaseExporter):
    def export(self):
        rows = self.fetch_all()
        columns = self.get_columns()
        filename = self.filename if self.filename.endswith(".csv") else self.filename + ".csv"

        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            for row in rows:
                writer.writerow([getattr(row, col) for col in columns])

        logger.info(f"Đã xuất bảng '{self.model_class.__tablename__}' ra CSV: {filename}")
