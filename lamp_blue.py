#!/usr/bin/env python

import sys
import os
import lamp_config

cmd = "curl -X PUT -d '{\"xy\":[0.159465946, 0.015232065]}' http://%s/api/%s/lights/1/state" % (lamp_config.ip, lamp_config.username)
print(cmd)
os.system(cmd)
print()
