import os

URL         = os.environ.get('OPENORDERS_DB_URL') or os.environ.get('DATABASE_URL')
DBNAME      = os.environ.get('OPENORDERS_DB_NAME') or 'openorders'
USERNAME    = os.environ.get('OPENORDERS_DB_USER') or 'openorders'
PORT        = os.environ.get('OPENORDERS_DB_PORT') or '5432'
HOST        = os.environ.get('OPENORDERS_DB_HOST') or 'localhost'
PASS        = os.environ.get('OPENORDERS_DB_PASS') or 'changeme'
