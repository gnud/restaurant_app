# logger_class = 'utils.SQLiteHandler.SQLiteHandler'
import os

host = os.environ.get('APP_HOST', '0.0.0.0')
port = int(os.environ.get('APP_PORT', 8000))
workers = os.environ.get('APP_WORKERS', 1)

bind = f'{host}:{port}'
loglevel = os.environ.get('APP_LOG_LEVEL', 'debug')
capture_output = True
