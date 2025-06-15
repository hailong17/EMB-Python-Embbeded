MySQL/
├── main.py
├── mydata.db
└── database/
│   ├── models.py
│   └── exporter/
│       ├── base_exporter.py
│       ├── excel_exporter.py
│       └── csv_exporter.py
└── utils/
    └── logger.py




#Create evn:
python -m venv .venv

.venv\Scripts\activate

#Install Requirements.txt
pip install -r requirements.txt

pip freeze > requirements.txt
