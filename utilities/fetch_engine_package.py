import json
import os


def main():
    print(os.path.abspath(os.path.curdir))
    with open(os.path.join(os.path.abspath(os.path.curdir), "settings.json"), "r") as sj:
        with open(os.path.join(os.path.abspath(os.path.curdir), "db_engine_list.json"), "r") as el:
            engine_list = json.load(el)
            print(type(engine_list))
        setting_list = json.load(sj)
    return [engine_list[v["engine"]] for v in setting_list["db_engines"].values()]


if __name__ == "__main__":
    print(main())
