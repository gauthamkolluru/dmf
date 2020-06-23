from pkgutil import iter_modules


def chk_mod(mod_name):
    return mod_name in [i.name for i in iter_modules()]


if __name__ == "__main__":
    print(chk_mod('os'))
