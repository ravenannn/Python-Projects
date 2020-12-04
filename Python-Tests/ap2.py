


import ap


def print_app2():
    name = (__name__)
    return name


if __name__ ==  "__main__":
    # The following is calling code from within the script
    print("I am running code from {}".format(print_app2()))

    # The following is calling code from within the imported ap.py
    print("I am running code from {}".format(ap.print_app()))
