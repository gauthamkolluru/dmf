from sqlalchemy.engine.url import URL as sql_url
from sqlalchemy import create_engine
from utilities.fetch_engine_package import pkg_details


def connection(ds_type):
    con_det = pkg_details(ds_type)
    return create_engine(sql_url(con_det['drivername'], username=con_det['user'], password=con_det['password'], host=con_det['host'], port=con_det['port'], database=con_det['database'], query=con_det['query']))


if __name__ == "__main__":
    print(connection('source'))
