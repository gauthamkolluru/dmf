import os
import json
import csv
from fsplit.filesplit import FileSplit
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
    db_det = pkg_details(ds_type)
    DB_URL_2 = repr(sql_url(db_det['drivername'],
                            username=db_det['username'],
                            password=db_det['password'],
                            host=db_det['host'],
                            port=db_det['port'],
                            database=db_det['database'],
                            query={"driver": "sql+server"}))
    return create_engine(DB_URL_2, echo=True), db_det['database']


def get_tables(conn):
    for table_name in conn.table_names():
        yield table_name


def get_table_data(conn, table_name):
    select_query = "select * from {}"
    table_data = conn.execute(select_query.format(table_name))
    return table_data.keys(), table_data.fetchall()


def write_csv(file_name='', file_data=None, file_ext='.csv'):
    with open(file_name+file_ext, 'w') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerows(file_data)
    return True


def split_csv(file_name='', file_ext='csv'):
    fs = FileSplit(file=".".join([file_name, file_ext]), splitsize=10)
    # fs = FileSplit(file=".".join([file_name, file_ext]), splitsize=1000000000)
    return fs.split(include_header=True)


def main():
    src_con, db_name = connection(DS_TYPES[0])
    src_con.connect()
    for table_name in get_tables(src_con):
        headers, data = get_table_data(src_con, table_name)
        data.insert(0, headers)
        file_name = "_".join([db_name, table_name])
        write_csv(file_name=file_name, file_data=data)
        split_csv(file_name=file_name)
    return True


if __name__ == "__main__":
    try:
        print(main())
    except Exception as e:
        print(e.__traceback__())
