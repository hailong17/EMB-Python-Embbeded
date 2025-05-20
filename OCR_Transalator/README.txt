ocr_translator_app/
├── main.py
├── ui/
│   └── app_ui.py
├── core/
│   ├── base_image_handler.py
│   ├── image_handler.py
│   ├── ocr_engine.py
│   └── translator.py
└── assets/
    └── captured.jpg (ảnh sẽ lưu tạm tại đây)

#Create evn:
python -m venv .venv

.venv\Scripts\activate

#Install Requirements.txt
pip install -r requirements.txt

pip freeze > requirements.txt
