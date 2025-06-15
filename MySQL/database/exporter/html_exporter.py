from database.models import User, get_engine, get_session
from utils.logger import logger
from database.exporter.base_exporter import BaseExporter
from jinja2 import Environment, FileSystemLoader
import os

class HTMLExporter(BaseExporter):
    def export(self, output_path="Output/users.html"):
        users = self.fetch_users()

        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("users_template.html")

        html_content = template.render(users=users)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        logger.info(f"✅ Đã xuất dữ liệu người dùng ra file HTML tại: {output_path}")
        logger.info(f"🌐 Mở trên trình duyệt: file://{os.path.abspath(output_path)}")
