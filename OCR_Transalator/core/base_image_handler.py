from abc import ABC, abstractmethod

class BaseImageHandler(ABC):
    def __init__(self):
        self.image_path = None

    @abstractmethod
    def load_image(self):
        pass
