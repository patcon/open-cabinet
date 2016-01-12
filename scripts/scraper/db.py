import os
import psycopg2
from psycopg2.pool import SimpleConnectionPool
import DBCONFIG
import contextlib
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
from psycopg2.extras import RealDictCursor

if DBCONFIG.URL:
    pool = SimpleConnectionPool(1,10, DBCONFIG.URL)
else:
    pool = SimpleConnectionPool(1,10, dbname=DBCONFIG.DBNAME, \
                                        user= DBCONFIG.USERNAME, \
                                        host= DBCONFIG.HOST, \
                                        port=DBCONFIG.PORT, \
                                        password=DBCONFIG.PASS)


@contextlib.contextmanager
def get_db(dictposs=False):
    con = pool.getconn()
    con.set_client_encoding('UTF8')
    if dictposs == True:
        con.cursor_factory = RealDictCursor    
    if dictposs != True:
        con.cursor_factory = None   
    try:
        yield con.cursor()
    finally:
        pool.putconn(con)


def create_db():
    with get_db() as cur:
        scraper_dir = os.path.dirname(__file__)
        schema_file_path = os.path.join(scraper_dir, "schema.sql")
        cur.execute(open(schema_file_path, "r").read())
        cur.connection.commit()