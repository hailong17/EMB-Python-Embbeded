from database.models import Base, User, get_engine, get_session
from database.exporter.excel_exporter import ExcelExporter
from database.exporter.csv_exporter import CSVExporter
from utils.logger import logger
from database.query_utils import UserService

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

    session = get_session(engine)
    if session.query(User).count() == 0:
        session.add_all([
            User(name="Long", email="long@example.com", phone=123456789),
            User(name="An", email="an@example.com", phone=987654321),
        ])
        session.commit()
        logger.info("✅ Đã thêm dữ liệu mẫu.")

def main():
    init_db()

    service = UserService()
    service.insert_user("Trang","tranglt23",123456)
    service.delete_user_by_email("an@example.com")
    service.list_users()

    # Export Excel
    exporter = ExcelExporter(User, filename="./Output/users.xlsx")
    exporter.export()

    # Export CSV
    csv_exporter = CSVExporter(User, filename="./Output/users.csv")
    csv_exporter.export()

    logger.info("✅ Export hoàn tất.")

if __name__ == "__main__":
    main()
