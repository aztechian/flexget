#!/usr/bin/env python

import flexget, sys, os

args = []
if os.environ.get('FG_CONFIG'):
  args.extend(["-c", os.environ.get('FG_CONFIG')])
if os.environ.get('FG_COMMAND'):
  args.extend(os.environ.get('FG_COMMAND','daemon start').split(' '))

if len(args) > 0:
  flexget.main(args)
else:
  flexget.main()
