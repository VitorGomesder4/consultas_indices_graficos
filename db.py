#Arquivo criador do banco e conexão para evitar multi-import

import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_DATABASE = os.getenv("DB_DATABASE")


db = sqlite3.connect(DB_DATABASE, check_same_thread=False)

print(db)