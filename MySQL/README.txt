MySQL/
│
├── main.py
├── mydata.db
└── database/
    ├── models.py
    └── exporter.py


#Create evn:
python -m venv .venv

.venv\Scripts\activate

#Install Requirements.txt
pip install -r requirements.txt

pip freeze > requirements.txt
