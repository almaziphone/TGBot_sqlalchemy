from pathlib import Path

from decouple import config

DIR = Path(__file__).absolute().parent

BOT_TOKEN = config('BOT_TOKEN')
ADMINS = [int(_) for _ in config('ADMINS', default='').split()]
RATE_LIMIT = config('RATE_LIMIT', default=0.5, cast=float)

DB_USER = config('DATABASE_USER', default=None)
DB_PASSWORD = config('DATABASE_PASS', default=None)
DB_HOST = config('DATABASE_HOST', default=None)
DB_PORT = config('DATABASE_PORT', default=5432)
if DB_PORT:
    DB_PORT = int(DB_PORT)
DB_NAME = config('DATABASE_NAME', default=None)

SQLALCHEMY_DATABASE_URI = f'sqlite+aiosqlite:///{DIR}/database.sqlite3'

if DB_USER and DB_PASSWORD and DB_HOST and DB_PORT and DB_NAME:
    SQLALCHEMY_DATABASE_URI = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

REDIS_HOST = config('REDIS_HOST', default=None)
REDIS_PORT = config('REDIS_PORT', default=6379)
REDIS_DB = config('REDIS_DB', default=5)

if REDIS_PORT:
    REDIS_PORT = int(REDIS_PORT)
if REDIS_DB:
    REDIS_DB = int(REDIS_DB)

WEBHOOK_PORT = config('WEBHOOK_PORT', default=8000)
WEBHOOK_HOST = config('WEBHOOK_HOST', default=None)
WEBHOOK_PATH = config('WEBHOOK_PATH', default=None)

if WEBHOOK_PORT:
    WEBHOOK_PORT = int(WEBHOOK_PORT)

I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}/locales'
