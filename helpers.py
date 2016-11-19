def bug(msg):
    """Debug output."""
    print "DEBUG: %s" % msg


def writeconf(file, content):
    """Write out config file."""
    print "INFO: writing %s" % file
    f = open(file, 'w')
    f.write(content)
    f.close()
