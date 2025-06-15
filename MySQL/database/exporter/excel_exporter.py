from openpyxl import Workbook
from .base_exporter import BaseExporter
from utils.logger import logger

class ExcelExporter(BaseExporter):
    def export(self):
        rows = self.fetch_all()
        columns = self.get_columns()
        filename = self.filename if self.filename.endswith(".xlsx") else self.filename + ".xlsx"

        wb = Workbook()
        ws = wb.active
        ws.title = self.model_class.__tablename__.capitalize()

        ws.append(columns)
        for row in rows:
            ws.append([getattr(row, col) for col in columns])

        wb.save(filename)
        logger.info(f"Đã xuất bảng '{self.model_class.__tablename__}' ra Excel: {filename}")
