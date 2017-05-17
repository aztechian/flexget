#!/usr/bin/env python

import flexget, sys, os

args = []
debug = os.environ.get('FG_DEBUG',False)
if debug in ['Yes','yes','true','True','on','1']:
  debug = True
if os.environ.get('FG_CONFIG'):
  args.extend(["-c", os.environ.get('FG_CONFIG')])
if os.environ.get('FG_COMMAND'):
  args.extend(os.environ.get('FG_COMMAND','daemon start').split(' '))

if len(args) > 0:
  if debug:
    print "Starting flexget with: %s" % args
  flexget.main(args)
else:
  flexget.main()
