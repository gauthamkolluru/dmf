import json
import os


def pkg_details(ds_type):
    print(os.path.abspath(os.path.curdir))
    if ds_type in ['source', 'destination']:
        with open(os.path.join(os.path.abspath(os.path.curdir), "settings.json"), "r") as sj:
            setting_list = json.load(sj)
        return setting_list["db_engines"][ds_type]
    return False


if __name__ == "__main__":
    det = pkg_details('destination')
    print(det)
