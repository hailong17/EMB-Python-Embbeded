from database.models import Base, User, get_engine, get_session
from database.exporter import UserExporter

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

    # Add sample data nếu bảng trống
    session = get_session(engine)
    if session.query(User).count() == 0:
        user1 = User(name="Long", email="long@example.com")
        user2 = User(name="An", email="an@example.com")
        session.add_all([user1, user2])
        session.commit()
        print("✅ Thêm dữ liệu mẫu vào database.")

def main():
    init_db()

    # Xuất dữ liệu ra Excel
    exporter = UserExporter()
    exporter.export_to_excel("users.xlsx")

if __name__ == "__main__":
    main()
