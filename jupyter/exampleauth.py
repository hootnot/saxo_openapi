# -*- coding: utf-8 -*-

def read_token(tokenFile="token.txt"):
    with open(tokenFile) as I:
        return I.read().strip()
