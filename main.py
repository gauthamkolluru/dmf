from connect import connection

DS_TYPES = ['source', 'destination']

def main():
    src_con = connection(DS_TYPES[0])

    dst_con = connection(DS_TYPES[1])
    return True


if __name__ == "__main__":
    print(main())
