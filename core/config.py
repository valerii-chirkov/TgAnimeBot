import os
from dotenv import load_dotenv


load_dotenv()


BOT_NAME = os.getenv('BOT_NAME')  # optional
ADMIN_ID = os.getenv('ADMIN_ID')
TOKEN = os.getenv('BOT_TOKEN')

DB_URL = os.getenv('DB_URL')
