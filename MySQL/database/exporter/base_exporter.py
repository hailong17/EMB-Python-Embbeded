from abc import ABC, abstractmethod
from sqlalchemy.inspection import inspect
from ..models import get_engine, get_session
from utils.logger import logger

class BaseExporter(ABC):
    def __init__(self, model_class, db_path="mydata.db", filename=None):
        self.model_class = model_class
        self.engine = get_engine(db_path)
        self.session = get_session(self.engine)
        self.filename = filename or f"{model_class.__tablename__}"
        logger.info(f"Khởi tạo exporter cho bảng '{self.model_class.__tablename__}'")

    def fetch_all(self):
        return self.session.query(self.model_class).all()

    def get_columns(self):
        return [col.name for col in inspect(self.model_class).columns]

    @abstractmethod
    def export(self):
        pass
