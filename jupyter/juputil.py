# -*- coding: utf-8 -*-


def read_token(tokenFile="token.txt"):
    with open(tokenFile) as FHtok:
        return FHtok.read().strip()


def request_info(r):
    """request_info = show some information for request instance r."""
    print("API-endpoint   : {}".format(r))
    print("METHOD         : {}".format(r.method))
    print("Response status: {}".format(r.status_code))
