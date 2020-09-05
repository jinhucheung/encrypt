#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import hashlib

root_path = os.path.sep.join([os.path.split(os.path.realpath(__file__))[0], '..'])

sys.path.append(root_path)
from lib import Config

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='example: python %s -p password' % os.path.basename(__file__))
    parser.add_argument('-p', '--password', help='password', required=True)
    args = parser.parse_args()

    password_slat = Config.get('slat', '') + args.password

    print(hashlib.md5(password_slat.encode()).hexdigest())