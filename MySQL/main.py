from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

# Kết nối SQLite - tạo file mydata.db (nếu chưa có)
engine = create_engine("sqlite:///mydata.db", echo=True)

# Khởi tạo base class cho ORM
Base = declarative_base()

# Định nghĩa bảng User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Tạo bảng nếu chưa có
Base.metadata.create_all(engine)

# Tạo session và thêm dữ liệu
with Session(engine) as session:
    # Thêm một user
    new_user = User(name="Long", email="long@example.com")
    session.add(new_user)
    session.commit()

    second_user = User(name="Hai", email="longnh63@example.com")
    session.add(second_user)
    session.commit()

    session.delete(new_user)
    session.commit()

    # Truy vấn tất cả user
    users = session.query(User).all()
    for user in users:
        print(f"{user.id}: {user.name} - {user.email}")
