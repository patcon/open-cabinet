import os

SECRET_KEY = os.environ.get('OPENORDERS_FLASK_SECRET') or 'your_secret_key'
DEBUG = os.environ.get('OPENORDERS_FLASK_DEBUG') in ['true', 'True', '1'] or True
