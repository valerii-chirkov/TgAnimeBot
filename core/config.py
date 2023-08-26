import os
from dotenv import load_dotenv


load_dotenv()


BOT_NAME = "ValeraSeriesBot"
ADMIN_ID = 209030944
TOKEN = os.getenv('BOT_TOKEN')

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_DATABASE = os.getenv('PG_DATABASE')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_COMMAND_TIMEOUT = os.getenv('PG_COMMAND_TIMEOUT')
