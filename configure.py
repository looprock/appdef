#!/usr/bin/env python
"""Create configurations."""
import yaml
import sys
# import json
from optparse import OptionParser
import batch

with open(sys.argv[1], 'r') as stream:
    try:
        appdef = yaml.load(stream)
        # print json.dumps(appdef, indent=4, sort_keys=True)
    except yaml.YAMLError as exc:
        print(exc)


# Command Line Arguments Parser
cmd_parser = OptionParser(version="%prog 0.1")
cmd_parser.add_option("-v", "--verbose", action="store_true", dest="bug", help="Enable debug mode")
cmd_parser.add_option("-t", "--type", type="string", action="store", dest="type", help="config type", default=None)
cmd_parser.add_option("-b", "--batch", type="string", action="store", dest="batch", help="config batch", default=None)
(cmd_options, cmd_args) = cmd_parser.parse_args()

# print appdef

if cmd_options.batch:
    x = getattr(batch, cmd_options.batch)(appdef)
