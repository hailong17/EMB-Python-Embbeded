from openpyxl import Workbook
from .models import User, get_engine, get_session

class UserExporter:
    def __init__(self, db_path: str = "mydata.db"):
        self.engine = get_engine(db_path)
        self.session = get_session(self.engine)

    def fetch_users(self):
        return self.session.query(User).all()

    def export_to_excel(self, filename: str = "users.xlsx"):
        users = self.fetch_users()
        wb = Workbook()
        ws = wb.active
        ws.title = "Users"

        # Header
        ws.append(["ID", "Name", "Email"])

        # Rows
        for user in users:
            ws.append([user.id, user.name, user.email])

        wb.save(filename)
        print(f"✅ Đã ghi {len(users)} users vào file '{filename}'")
