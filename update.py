#!/usr/bin/env python

import sys
import os
import re

if sys.version_info.major >= 3:
    import urllib.request

    r = urllib.request.urlopen('https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    assert r.status == 200
    data = r.read().decode('utf-8').split('\n')
else:
    import urllib

    r = urllib.urlopen('https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    assert r.getcode() == 200
    data = r.read().split('\n')

version = re.match('^# Version (?P<version>[0-9]+).*$', data[0]).group('version')
tlds = [i.lower() for i in data[1:] if i and not i.startswith('#')]


target_dir = 'tlds'

with open(os.path.join(target_dir, '_data.py'), 'w') as f:
    f.write('tld_set = set(%s)\n' % (tlds, ))

with open('version.py', 'w') as f:
    f.write('version = %s\n' % version)
