#!/usr/bin/env python
"""Create configurations."""
import yaml
from optparse import OptionParser
import batch


# Command Line Arguments Parser
cmd_parser = OptionParser(version="%prog 0.1")
cmd_parser.add_option("-v", "--verbose", action="store_true", dest="bug", help="Enable debug mode")
cmd_parser.add_option("-t", "--type", type="string", action="store", dest="type", help="config type", default=None)
cmd_parser.add_option("-b", "--batch", type="string", action="store", dest="batch", help="config batch", default=None)
(cmd_options, cmd_args) = cmd_parser.parse_args()


with open(cmd_args[0], 'r') as stream:
    try:
        appdef = yaml.load(stream)
        # print json.dumps(appdef, indent=4, sort_keys=True)
    except yaml.YAMLError as exc:
        print(exc)

if cmd_options.batch:
    try:
        x = getattr(batch, cmd_options.batch)(appdef)
    except AttributeError:
        print "ERROR: batch method %s not found!" % cmd_options.batch
