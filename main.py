import json
from sqlalchemy.engine.url import URL as sql_url
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base


DS_TYPES = ['source', 'destination']

Base = declarative_base()


def pkg_details(ds_type):
    with open("./settings.json", "r") as sj:
        setting_list = json.load(sj)
    return setting_list["db_engines"][ds_type] if setting_list else False


def connection(ds_type):
    con_det = pkg_details(ds_type)
    DB_URL = "{}://{}/{}?driver=sql+server".format(
        con_det['drivername'], con_det['host'], con_det['database'])
    # DB_URL = sql_url(con_det['drivername'], host=con_det['host'], database=con_det['database'], query="driver=sql+server")
    print(DB_URL)
    return create_engine(DB_URL, echo=True)


def get_tables():
    return


def main():
    src_con = connection(DS_TYPES[0])
    src_con.connect()
    META_DATA = MetaData(bind=src_con)
    META_DATA.reflect()
    for tbl in META_DATA.tables:
        print(tbl)
    return True


if __name__ == "__main__":
    try:
        print(main())
    except Exception as e:
        e.__traceback__
