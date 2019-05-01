#!/usr/bin/env python
from __future__ import print_function, absolute_import

import argparse
import logging
import os.path
import sys
from . import settings
from .create import create
from .update import update
from .extract import extract
from .chgrp import chgrp
from .check import check
from .ls import ls


# -----------------------------------------------------------------------------
def main():

    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)
    parser = argparse.ArgumentParser(
        usage='''zstash <command> [<args>]

Available zstash commands:
  create     create new archive
  update     update existing archive
  extract    extract files from archive
  chgrp      change the group of an archive
  check      check the integrity of the files in the archive
  ls         list the files in an archive

For help with a specific command
  zstash command --help
''')
    parser.add_argument('command',
                        help='command to run (create, update, extract, ...)')
    # parse_args defaults to [1:] for args, but you need to
    # exclude the rest of the args too, or validation will fail
    args = parser.parse_args(sys.argv[1:2])

    if args.command == 'create':
        create()
    elif args.command == 'update':
        update()
    elif args.command == 'extract':
        extract()
    elif args.command == 'chgrp':
        chgrp()
    elif args.command == 'check':
        check()
    elif args.command == 'ls':
        ls()
    else:
        print('Unrecognized command')
        parser.print_help()
        sys.exit(1)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
