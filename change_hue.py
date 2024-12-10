#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
  print("""
Usage: change_hue.py <hue>

hue: is an integer 0-65535, corresponding to the colorwheel from red to red""")
  sys.exit(1)

cmd = "curl -X PUT -d '{\"hue\":%d}' http://192.168.1.50/api/2PZVBMRs12EovMoeBtcNADFRdzg8I-ujlAXp-VjL/lights/1/state" % (int(sys.argv[1]))
print(cmd)
os.system(cmd)
print()
