#!/bin/env python2
from remotsylib import api
import argparse
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store", type=str, required=True)
    parser.add_argument("-p", "--password", action="store", type=str, required=True)
    args =  parser.parse_args(sys.argv[1:])

    client = api.Api()
    token = client.login(args.username, args.password)
    print(token)
    lst_ctl = client.list_controls()
    for ctl in lst_ctl:
        print "id %s Name %s" % (ctl["_id"], ctl['name'])
