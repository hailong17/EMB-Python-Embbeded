from database.models import User, get_engine, get_session
from utils.logger import logger

class UserService:
    def __init__(self, db_path="mydata.db"):
        self.engine = get_engine(db_path)
        self.session = get_session(self.engine)

    def insert_user(self, name, email, phone):
        new_user = User(name=name, email=email, phone=phone)
        self.session.add(new_user)
        self.session.commit()
        logger.info(f"Thêm user: {name} ({email})")

    def delete_user_by_email(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            logger.info(f"Đã xóa user với email: {email}")
        else:
            logger.warning(f"Không tìm thấy user với email: {email}")

    def list_users(self):
        users = self.session.query(User).all()
        for user in users:
            print(f"- {user.name} ({user.email}, {user.phone})")
