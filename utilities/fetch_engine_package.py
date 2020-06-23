import json
import os

print(os.path.realpath('.'))


def pkg_details(ds_type):
    print(os.path.abspath(os.path.curdir), "pkg_details func")
    if ds_type in ['source', 'destination']:
        with open(os.path.join(os.path.realpath('.'), "settings.json"), "r") as sj:
            setting_list = json.load(sj)
        return setting_list["db_engines"][ds_type]
    return False


if __name__ == "__main__":
    det = pkg_details('destination')
    print(det)


# TODO:

# 1. figureout a consistent way to deal with the paths
