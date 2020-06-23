from connect import connection


def main():
    src_con = connection('source')

    dst_con = connection('destination')
    return True


if __name__ == "__main__":
    print(main())
