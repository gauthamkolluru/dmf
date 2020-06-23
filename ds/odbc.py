from chk_mod import chk_mod

MODULE_NAME = 'pyodbc'


def import_module():
    if chk_mod(MODULE_NAME):
        import os
        return True
    print("Please install the required " + MODULE_NAME + " and continue")
    return False


if __name__ == "__main__":
    import_module()
